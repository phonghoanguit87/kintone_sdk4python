#!/usr/bin/env python
# -*- coding: utf_8 -*-
from .kintone_sdk import Kintone

__author__ = 'sadaya-nishio'
__version__ = '0.0.1'
__license__ = 'MIT License'

kintone = Kintone()
kintone.set_domain('hw1xj.cybozu.com')
kintone.set_user_auth('sadaya-nishio', 'sadaya-nishio')
#kintone.set_token_auth('6kSjeYGjxetmNmLs8xWsOB1T5EhCa5AiKaHjPBYT')
#record = kintone.get_record(328, 10)
records = kintone.get_records(328, '自動採番 like "15-00015"', ['レコード番号', '$id'], True)
records2 = kintone.get_records(328, '自動採番 like "15-00015"', ['自動採番'], True)
print(records)
print(records2)