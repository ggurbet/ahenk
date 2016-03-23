#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>

import threading

from base.task.TaskJob import TaskJob


class TaskInQueue(threading.Thread):
    """docstring for TaskInQueue"""

    def __init__(self, inQueue):
        super(TaskInQueue, self).__init__()
        self.inQueue = inQueue

    def run(self):
        # Add task to db. Adding task to db important because task can be lost when processing.
        # Call plugin manager and process message inside task job
        try:
            task = self.inQueue.get()
            print(task)
            # Can be validate task before processing
            job = TaskJob(task)
            job.start()

        except Exception as e:
            raise
