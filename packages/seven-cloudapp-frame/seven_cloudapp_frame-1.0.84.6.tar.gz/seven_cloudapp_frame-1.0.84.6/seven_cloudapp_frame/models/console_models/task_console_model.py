# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-07-19 13:37:16
@LastEditTime: 2023-05-22 18:50:53
@LastEditors: HuangJianYi
@Description: 
"""
import threading
from seven_framework.console.base_console import *
from seven_cloudapp_frame.models.enum import *
from seven_cloudapp_frame.models.frame_base_model import *
from seven_cloudapp_frame.libs.customize.seven_helper import *
from seven_cloudapp_frame.libs.common import *
from seven_cloudapp_frame.models.db_models.task.task_gear_count_model import *
from seven_cloudapp_frame.models.db_models.task.task_info_model import *
from seven_cloudapp_frame.models.db_models.task.task_count_model import *


class TaskConsoleModel():
    """
    :description: 任务控制台业务模型
    """

    def console_task_queue(self):
        """
        :description: 控制台统计上报
        :return: 
        :last_editors: HuangJianYi
        """
        for i in range(10):
            j = threading.Thread(target=self.process_task_queue, args=[i])
            j.start()

    def __get_task_gear_count(self, act_id, module_id, task_type, complete_type, user_id, task_gear_count_model):
        """
        :description: 获取当前任务档位计数
        :param act_id: 活动标识
        :param module_id: 模块标识
        :param task_type: 任务类型
        :param complete_type: 完成类型
        :param user_id: 用户标识
        :param task_gear_count_model: task_gear_count_model
        :return: 
        :last_editors: HuangJianYi
        """
        condition_where = ConditionWhere()
        condition_where.add_condition("act_id=%s and task_type=%s and user_id=%s")
        params = [act_id, task_type, user_id]
        if complete_type == TaskCompleteType.day.value:
            condition_where.add_condition("create_day=%s")
            params.append(SevenHelper.get_now_day_int())
        elif complete_type == TaskCompleteType.week.value:
            start_day = int(TimeHelper.get_first_day_of_the_week().strftime('%Y%m%d'))
            end_day = int(TimeHelper.get_last_day_of_the_week().strftime('%Y%m%d'))
            condition_where.add_condition("create_day>=%s and create_day<=%s")
            params.append(start_day)
            params.append(end_day)
        elif complete_type == TaskCompleteType.month.value:
            condition_where.add_condition("create_month=%s")
            params.append(SevenHelper.get_now_month_int())
        if module_id:
            condition_where.add_condition("module_id=%s")
            params.append(module_id)
        task_gear_count_dict = task_gear_count_model.get_dict(condition_where.to_string(),field="sum(now_count) as now_count",params=params)
        if task_gear_count_dict:
            return task_gear_count_dict["now_count"]
        else:
            return 0

    def process_task_queue(self, mod_value):
        """
        :description: 处理档位任务队列
        :param mod_value: 当前队列值
        :return: 
        :last_editors: HuangJianYi
        """
        print(f"{TimeHelper.get_now_format_time()} 档位任务队列{mod_value}启动")

        while True:
            try:
                time.sleep(0.1)

                redis_init = SevenHelper.redis_init()
                redis_key = f"task_gear_list:{mod_value}"
                task_queue_json = redis_init.lindex(redis_key, index=0)
                if not task_queue_json:
                    time.sleep(1)
                    continue
                try:
                    create_day = SevenHelper.get_now_day_int()
                    create_month = SevenHelper.get_now_month_int()
                    task_queue_dict = SevenHelper.json_loads(task_queue_json)
                    task_info_model = TaskInfoModel()
                    db_transaction = DbTransaction(db_config_dict=config.get_value("db_cloudapp"))
                    task_count_model = TaskCountModel(sub_table=FrameBaseModel().get_business_sub_table("task_log_tb", {"app_id": task_queue_dict["app_id"]}), db_transaction=db_transaction)
                    task_gear_count_model = TaskGearCountModel(db_transaction=db_transaction)
                    task_info_dict = task_info_model.get_dict("act_id=%s and module_id=%s and task_type=%s", params=[task_queue_dict["act_id"], task_queue_dict["module_id"], task_queue_dict["task_type"]])

                    task_gear_count = task_gear_count_model.get_entity("act_id=%s and task_type=%s and user_id=%s and create_day=%s and module_id=%s", params=[task_queue_dict["act_id"], task_queue_dict["task_type"], task_queue_dict["user_id"], create_day, task_queue_dict["module_id"]])
                    db_transaction.begin_transaction()
                    if not task_gear_count:
                        task_gear_count = TaskGearCount()
                        task_gear_count.app_id = task_queue_dict["app_id"]
                        task_gear_count.act_id = task_queue_dict["act_id"]
                        task_gear_count.module_id = task_queue_dict["module_id"]
                        task_gear_count.user_id = task_queue_dict["user_id"]
                        task_gear_count.open_id = task_queue_dict["open_id"]
                        task_gear_count.task_type = task_queue_dict["task_type"]
                        task_gear_count.now_count = task_queue_dict["now_count"]
                        task_gear_count.create_day = create_day
                        task_gear_count.create_month = create_month
                        task_gear_count.create_date = SevenHelper.get_now_datetime()
                        task_gear_count.remark = task_queue_dict["remark"]
                        task_gear_count_model.add_entity(task_gear_count)
                    else:
                        task_gear_count.remark = task_gear_count.remark + "," + task_queue_dict["remark"] if  task_gear_count.remark else task_queue_dict["remark"]
                        task_gear_count_model.update_table("now_count=now_count+%s,remark=%s,modify_date=%s", "id=%s", params=[task_queue_dict["now_count"], task_gear_count.remark, SevenHelper.get_now_datetime(), task_gear_count.id])
                    if task_info_dict:
                        now_count = self.__get_task_gear_count(task_queue_dict["act_id"],task_queue_dict["module_id"], task_queue_dict["task_type"], task_info_dict["complete_type"], task_queue_dict["user_id"], task_gear_count_model) + task_queue_dict["now_count"]
                        #判断子任务是否完成
                        config_json = SevenHelper.json_loads(task_info_dict["config_json"])
                        if config_json and config_json.__contains__("gear_list"):
                            config_json = config_json["gear_list"]
                            for sub_config_json in config_json:
                                task_count_id_md5 = CryptoHelper.md5_encrypt_int(f"{task_queue_dict['act_id']}_{task_queue_dict['module_id']}_{task_queue_dict['task_type']}_{sub_config_json['id']}_{task_queue_dict['user_id']}")
                                if decimal.Decimal(now_count) >= decimal.Decimal(sub_config_json["gear"]):
                                    task_count = TaskCount()
                                    task_count.id_md5 = task_count_id_md5
                                    task_count.app_id = task_queue_dict["app_id"]
                                    task_count.act_id = task_queue_dict["act_id"]
                                    task_count.module_id = task_queue_dict["module_id"]
                                    task_count.user_id = task_queue_dict["user_id"]
                                    task_count.open_id = task_queue_dict["open_id"]
                                    task_count.task_type = task_queue_dict["task_type"]
                                    task_count.task_sub_type = sub_config_json["id"]
                                    task_count.complete_count = 0
                                    task_count.now_count = 1
                                    task_count.create_date = SevenHelper.get_now_datetime()
                                    task_count.modify_date = SevenHelper.get_now_datetime()
                                    task_count.modify_day = SevenHelper.get_now_day_int()
                                    task_count_model.add_update_entity(task_count, "complete_count=0,now_count=1,modify_date=%s,modify_day=%s", params=[task_count.modify_date, task_count.modify_day])

                    result, message = db_transaction.commit_transaction(True)
                    if result == False:
                        raise Exception("执行事务失败", message)
                    redis_init.lpop(redis_key)

                except Exception as ex:
                    logger_error.error(f"档位任务队列{mod_value}异常,json串:{SevenHelper.json_dumps(task_queue_dict)},ex:{traceback.format_exc()}")
                    continue

            except Exception as ex:
                logger_error.error(f"档位任务队列{mod_value}异常,ex:{traceback.format_exc()}")
                time.sleep(5)
