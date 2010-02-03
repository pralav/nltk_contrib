#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

"""Chinese foreign-word-specific token extractor class.
"""

__author__ = """
rws@uiuc.edu (Richard Sproat)
"""

import extractor
import tokens
import Utils.script
from __init__ import BASE_

MIN_LEN_ = 3

CDOT_ = '・'

FOREIGN_CHARS_ = {
    "丁" : 1,
    "乃" : 1,
    "三" : 1,
    "凡" : 1,
    "土" : 1,
    "士" : 1,
    "夕" : 1,
    "大" : 1,
    "山" : 1,
    "不" : 1,
    "丹" : 1,
    "什" : 1,
    "内" : 1,
    "厄" : 1,
    "及" : 1,
    "夫" : 1,
    "太" : 1,
    "巴" : 1,
    "日" : 1,
    "比" : 1,
    "牙" : 1,
    "他" : 1,
    "加" : 1,
    "北" : 1,
    "卡" : 1,
    "可" : 1,
    "史" : 1,
    "尼" : 1,
    "布" : 1,
    "打" : 1,
    "旦" : 1,
    "本" : 1,
    "瓜" : 1,
    "瓦" : 1,
    "甘" : 1,
    "生" : 1,
    "白" : 1,
    "立" : 1,
    "伊" : 1,
    "列" : 1,
    "印" : 1,
    "吉" : 1,
    "地" : 1,
    "圭" : 1,
    "多" : 1,
    "安" : 1,
    "托" : 1,
    "朵" : 1,
    "汗" : 1,
    "百" : 1,
    "米" : 1,
    "耳" : 1,
    "艾" : 1,
    "衣" : 1,
    "西" : 1,
    "佛" : 1,
    "伯" : 1,
    "克" : 1,
    "利" : 1,
    "宋" : 1,
    "希" : 1,
    "杜" : 1,
    "杉" : 1,
    "沙" : 1,
    "罕" : 1,
    "贝" : 1,
    "辛" : 1,
    "那" : 1,
    "里" : 1,
    "亚" : 1,
    "亚" : 1,
    "佳" : 1,
    "来" : 1,
    "典" : 1,
    "坡" : 1,
    "坦" : 1,
    "奈" : 1,
    "姆" : 1,
    "孟" : 1,
    "定" : 1,
    "尚" : 1,
    "居" : 1,
    "冈" : 1,
    "帕" : 1,
    "底" : 1,
    "拉" : 1,
    "易" : 1,
    "昂" : 1,
    "明" : 1,
    "果" : 1,
    "林" : 1,
    "松" : 1,
    "河" : 1,
    "波" : 1,
    "法" : 1,
    "治" : 1,
    "肯" : 1,
    "芭" : 1,
    "芬" : 1,
    "金" : 1,
    "门" : 1,
    "陀" : 1,
    "阿" : 1,
    "阿" : 1,
    "保" : 1,
    "俄" : 1,
    "南" : 1,
    "哇" : 1,
    "哈" : 1,
    "奎" : 1,
    "威" : 1,
    "度" : 1,
    "律" : 1,
    "拜" : 1,
    "柯" : 1,
    "查" : 1,
    "柏" : 1,
    "洛" : 1,
    "玻" : 1,
    "科" : 1,
    "突" : 1,
    "约" : 1,
    "美" : 1,
    "耶" : 1,
    "茅" : 1,
    "英" : 1,
    "迦" : 1,
    "迪" : 1,
    "伦" : 1,
    "哥" : 1,
    "埃" : 1,
    "夏" : 1,
    "库" : 1,
    "恩" : 1,
    "拿" : 1,
    "朗" : 1,
    "根" : 1,
    "格" : 1,
    "泰" : 1,
    "浦" : 1,
    "海" : 1,
    "乌" : 1,
    "特" : 1,
    "班" : 1,
    "索" : 1,
    "纽" : 1,
    "纳" : 1,
    "兹" : 1,
    "茨" : 1,
    "马" : 1,
    "勒" : 1,
    "曼" : 1,
    "基" : 1,
    "培" : 1,
    "婆" : 1,
    "密" : 1,
    "仑" : 1,
    "康" : 1,
    "得" : 1,
    "理" : 1,
    "毕" : 1,
    "莎" : 1,
    "莫" : 1,
    "莉" : 1,
    "荷" : 1,
    "都" : 1,
    "雪" : 1,
    "麦" : 1,
    "麻" : 1,
    "凯" : 1,
    "博" : 1,
    "喀" : 1,
    "喜" : 1,
    "乔" : 1,
    "堪" : 1,
    "堡" : 1,
    "几" : 1,
    "敦" : 1,
    "斐" : 1,
    "斯" : 1,
    "普" : 1,
    "森" : 1,
    "汤" : 1,
    "犹" : 1,
    "琴" : 1,
    "答" : 1,
    "丝" : 1,
    "舒" : 1,
    "华" : 1,
    "莱" : 1,
    "菲" : 1,
    "贺" : 1,
    "买" : 1,
    "开" : 1,
    "隆" : 1,
    "雅" : 1,
    "黑" : 1,
    "塞" : 1,
    "塞" : 1,
    "塔" : 1,
    "奥" : 1,
    "爱" : 1,
    "新" : 1,
    "瑟" : 1,
    "瑞" : 1,
    "圣" : 1,
    "蒂" : 1,
    "叶" : 1,
    "路" : 1,
    "达" : 1,
    "雷" : 1,
    "顿" : 1,
    "嫩" : 1,
    "汉" : 1,
    "满" : 1,
    "尔" : 1,
    "玛" : 1,
    "福" : 1,
    "维" : 1,
    "蒙" : 1,
    "盖" : 1,
    "宾" : 1,
    "赫" : 1,
    "魁" : 1,
    "德" : 1,
    "慕" : 1,
    "摩" : 1,
    "撒" : 1,
    "撒" : 1,
    "潘" : 1,
    "热" : 1,
    "鲁" : 1,
    "黎" : 1,
    "墨" : 1,
    "卢" : 1,
    "翰" : 1,
    "诺" : 1,
    "赖" : 1,
    "锡" : 1,
    "弥" : 1,
    "济" : 1,
    "赛" : 1,
    "迈" : 1,
    "萨" : 1,
    "琼" : 1,
    "罗" : 1,
    "腊" : 1,
    "颠" : 1,
    "苏" : 1,
    "兰" : 1,
    "铁" : 1,
    "露" : 1,
    "璐" : 1,
    "朱" : 1,
    "娅" : 1,
    "默" : 1,
#    "・" : 1,
    "戴" : 1,
    "卓" : 1,
    "白" : 1,
    "艾" : 1,
    "爱" : 1,
    "阿" : 1,
    "埃" : 1,
    "底" : 1,
    "旦" : 1,
    "丹" : 1,
#    "・" : 1,
    "卡" : 1,
    "孔" : 1,
    "喀" : 1,
    "堪" : 1,
    "康" : 1,
    "凯" : 1,
    "法" : 1,
    "范" : 1,
    "甫" : 1,
    "傅" : 1,
    "福" : 1,
    "弗" : 1,
    "定" : 1,
    "恩" : 1,
    "冬" : 1,
    "鼎" : 1,
    "丁" : 1,
    "贝" : 1,
    "鲍" : 1,
    "堡" : 1,
    "保" : 1,
    "北" : 1,
    "都" : 1,
    "及" : 1,
    "几" : 1,
    "娇" : 1,
    "蕉" : 1,
    "本" : 1,
    "吉" : 1,
    "悸" : 1,
    "济" : 1,
    "九" : 1,
    "金" : 1,
    "叫" : 1,
    "卷" : 1,
    "佳" : 1,
    "窖" : 1,
    "加" : 1,
    "简" : 1,
    "剪" : 1,
    "贾" : 1,
    "居" : 1,
    "爵" : 1,
    "晋" : 1,
    "杰" : 1,
    "捷" : 1,
    "狗" : 1,
    "苟" : 1,
    "贡" : 1,
    "古" : 1,
    "姑" : 1,
    "圭" : 1,
    "瓜" : 1,
    "果" : 1,
    "哈" : 1,
    "安" : 1,
    "坎" : 1,
    "凡" : 1,
    "波" : 1,
    "卜" : 1,
    "不" : 1,
    "博" : 1,
    "伯" : 1,
    "玻" : 1,
    "布" : 1,
    "勃" : 1,
    "猜" : 1,
    "查" : 1,
    "仓" : 1,
    "怀" : 1,
    "冻" : 1,
    "长" : 1,
    "臣" : 1,
    "楚" : 1,
    "开" : 1,
    "华" : 1,
    "岑" : 1,
    "岱" : 1,
    "噶" : 1,
    "哩" : 1,
    "恋" : 1,
    "练" : 1,
    "莲" : 1,
    "廉" : 1,
    "立" : 1,
    "班" : 1,
    "多" : 1,
    "来" : 1,
    "雷" : 1,
    "腊" : 1,
    "赖" : 1,
    "拉" : 1,
    "坤" : 1,
    "昆" : 1,
    "库" : 1,
    "奥" : 1,
    "德" : 1,
    "柯" : 1,
    "嘎" : 1,
    "伦" : 1,
    "卢" : 1,
    "娄" : 1,
    "隆" : 1,
    "路" : 1,
    "露" : 1,
    "芭" : 1,
    "杜" : 1,
    "努" : 1,
    "纽" : 1,
    "诺" : 1,
    "奴" : 1,
    "典" : 1,
    "夸" : 1,
    "朵" : 1,
    "茨" : 1,
    "默" : 1,
    "摩" : 1,
    "沫" : 1,
    "姆" : 1,
    "墨" : 1,
    "漠" : 1,
    "得" : 1,
    "明" : 1,
    "米" : 1,
    "梅" : 1,
    "毛" : 1,
    "茅" : 1,
    "芒" : 1,
    "兰" : 1,
    "慕" : 1,
    "木" : 1,
    "虏" : 1,
    "莱" : 1,
    "鲁" : 1,
    "琅" : 1,
    "吕" : 1,
    "洛" : 1,
    "帕" : 1,
    "培" : 1,
    "佩" : 1,
    "莫" : 1,
    "尼" : 1,
    "穆" : 1,
    "拿" : 1,
    "美" : 1,
    "沐" : 1,
    "缅" : 1,
    "门" : 1,
    "沛" : 1,
    "狼" : 1,
    "那" : 1,
    "列" : 1,
    "祖" : 1,
    "锋" : 1,
    "娣" : 1,
    "娅" : 1,
    "姗" : 1,
    "科" : 1,
    "菲" : 1,
    "皮" : 1,
    "黎" : 1,
    "朗" : 1,
    "麻" : 1,
    "律" : 1,
    "玛" : 1,
    "迦" : 1,
    "抨" : 1,
    "潘" : 1,
    "纳" : 1,
    "娜" : 1,
    "乃" : 1,
    "蒙" : 1,
    "汶" : 1,
    "撇" : 1,
    "媛" : 1,
    "坡" : 1,
    "婆" : 1,
    "婷" : 1,
    "奇" : 1,
    "齐" : 1,
    "浦" : 1,
    "普" : 1,
    "七" : 1,
    "廖" : 1,
    "理" : 1,
    "劳" : 1,
    "里" : 1,
    "马" : 1,
    "彭" : 1,
    "蓬" : 1,
    "耐" : 1,
    "念" : 1,
    "奈" : 1,
    "娘" : 1,
    "南" : 1,
    "孟" : 1,
    "嵊" : 1,
    "烈" : 1,
    "林" : 1,
    "琳" : 1,
    "柳" : 1,
    "莉" : 1,
    "丽" : 1,
    "勒" : 1,
    "麦" : 1,
    "买" : 1,
    "迈" : 1,
    "仑" : 1,
    "庞" : 1,
    "浜" : 1,
    "弥" : 1,
    "秘" : 1,
    "溥" : 1,
    "龙" : 1,
    "蕾" : 1,
    "利" : 1,
    "满" : 1,
    "蔓" : 1,
    "曼" : 1,
    "内" : 1,
    "涅" : 1,
    "嫩" : 1,
    "密" : 1,
    "恺" : 1,
    "妮" : 1,
    "罗" : 1,
    "哥" : 1,
    "绛" : 1,
    "登" : 1,
    "壳" : 1,
    "盖" : 1,
    "恰" : 1,
    "羌" : 1,
    "卿" : 1,
    "乔" : 1,
    "丘" : 1,
    "切" : 1,
    "珀" : 1,
    "琼" : 1,
    "缪" : 1,
    "茄" : 1,
    "钦" : 1,
    "沁" : 1,
    "琴" : 1,
    "答" : 1,
    "佛" : 1,
    "葛" : 1,
    "娥" : 1,
    "谢" : 1,
    "肖" : 1,
    "歇" : 1,
    "辛" : 1,
    "欣" : 1,
    "新" : 1,
    "信" : 1,
    "袖" : 1,
    "星" : 1,
    "休" : 1,
    "玄" : 1,
    "可" : 1,
    "莎" : 1,
    "森" : 1,
    "僧" : 1,
    "桑" : 1,
    "璐" : 1,
    "瑙" : 1,
    "兹" : 1,
    "度" : 1,
    "比" : 1,
    "搓" : 1,
    "戈" : 1,
    "臧" : 1,
    "甘" : 1,
    "士" : 1,
    "史" : 1,
    "诗" : 1,
    "施" : 1,
    "圣" : 1,
    "冯" : 1,
    "八" : 1,
    "邓" : 1,
    "克" : 1,
    "彼" : 1,
    "索" : 1,
    "丝" : 1,
    "朔" : 1,
    "帅" : 1,
    "杉" : 1,
    "山" : 1,
    "冉" : 1,
    "斯" : 1,
    "什" : 1,
    "槌" : 1,
    "沙" : 1,
    "瑟" : 1,
    "舍" : 1,
    "儒" : 1,
    "茹" : 1,
    "抒" : 1,
    "舒" : 1,
    "尚" : 1,
    "瑞" : 1,
    "枭" : 1,
    "热" : 1,
    "松" : 1,
    "颂" : 1,
    "宋" : 1,
    "珊" : 1,
    "若" : 1,
    "撒" : 1,
    "戎" : 1,
    "日" : 1,
    "萨" : 1,
    "苏" : 1,
    "滕" : 1,
    "生" : 1,
    "塞" : 1,
    "赛" : 1,
    "他" : 1,
    "三" : 1,
    "绳" : 1,
    "兽" : 1,
    "塔" : 1,
    "俄" : 1,
    "巴" : 1,
    "汀" : 1,
    "突" : 1,
    "桐" : 1,
    "廷" : 1,
    "黛" : 1,
    "嘴" : 1,
    "太" : 1,
    "泰" : 1,
    "邦" : 1,
    "孜" : 1,
    "滴" : 1,
    "西" : 1,
    "维" : 1,
    "韦" : 1,
    "达" : 1,
    "迪" : 1,
    "肯" : 1,
    "毕" : 1,
    "夕" : 1,
    "席" : 1,
    "希" : 1,
    "图" : 1,
    "坦" : 1,
    "喜" : 1,
    "斐" : 1,
    "土" : 1,
    "吐" : 1,
    "汤" : 1,
    "温" : 1,
    "铄" : 1,
    "毋" : 1,
    "箱" : 1,
    "夏" : 1,
    "唐" : 1,
    "托" : 1,
    "勿" : 1,
    "惕" : 1,
    "伍" : 1,
    "仙" : 1,
    "臀" : 1,
    "翁" : 1,
    "陀" : 1,
    "禅" : 1,
    "特" : 1,
    "魏" : 1,
    "沃" : 1,
    "瓦" : 1,
    "旺" : 1,
    "哇" : 1,
    "忘" : 1,
    "铁" : 1,
    "乌" : 1,
    "梯" : 1,
    "锡" : 1,
    "威" : 1,
    "娃" : 1,
    "格" : 1,
    "笛" : 1,
    "费" : 1,
    "炎" : 1,
    "选" : 1,
    "逊" : 1,
    "雪" : 1,
    "牙" : 1,
    "雅" : 1,
    "袂" : 1,
    "亚" : 1,
    "扬" : 1,
    "延" : 1,
    "演" : 1,
    "昂" : 1,
    "含" : 1,
    "海" : 1,
    "罕" : 1,
    "大" : 1,
    "庇" : 1,
    "莹" : 1,
    "印" : 1,
    "英" : 1,
    "打" : 1,
    "夫" : 1,
    "厄" : 1,
    "狄" : 1,
    "芬" : 1,
    "易" : 1,
    "叶" : 1,
    "耶" : 1,
    "尧" : 1,
    "佐" : 1,
    "霍" : 1,
    "冈" : 1,
    "宰" : 1,
    "裕" : 1,
    "钓" : 1,
    "宾" : 1,
    "芝" : 1,
    "斋" : 1,
    "乍" : 1,
    "柏" : 1,
    "地" : 1,
    "敦" : 1,
    "咏" : 1,
    "约" : 1,
    "汗" : 1,
    "翰" : 1,
    "詹" : 1,
    "亨" : 1,
    "豪" : 1,
    "伊" : 1,
    "衣" : 1,
    "义" : 1,
    "珍" : 1,
    "宙" : 1,
    "銮" : 1,
    "荷" : 1,
    "尤" : 1,
    "鲫" : 1,
    "侯" : 1,
    "何" : 1,
    "犹" : 1,
    "朱" : 1,
    "治" : 1,
    "蹴" : 1,
    "汉" : 1,
    "河" : 1,
    "赫" : 1,
    "贺" : 1,
    "艺" : 1,
    "泽" : 1,
    "趄" : 1,
    "哉" : 1,
    "拄" : 1,
    "胡" : 1,
    "黑" : 1,
    "扎" : 1,
    "赞" : 1,
    "颠" : 1,
    "叻" : 1,
    "耳" : 1,
    "讪" : 1,
    "讷" : 1,
    "诋" : 1,
    "根" : 1,
    "基" : 1,
    "踪" : 1,
    "百" : 1,
    "蒂" : 1,
    "顿" : 1,
    "蝶" : 1,
    "尔" : 1,
    "迭" : 1,
    "奎" : 1,
    "芙" : 1,
    "茜" : 1,
    "衮" : 1,
    "魁" : 1,
    "拜" : 1,
    "炳" : 1,
    "薇" : 1}

FAMILY_NAMES_ = {
  "丁" : 1,
  "万" : 1,
  "丘" : 1,
  "丛" : 1,
  "严" : 1,
  "乌" : 1,
  "乐" : 1,
  "乔" : 1,
  "于" : 1,
  "亓" : 1,
  "仇" : 1,
  "仝" : 1,
  "仲" : 1,
  "任" : 1,
  "伍" : 1,
  "伏" : 1,
  "但" : 1,
  "佐" : 1,
  "何" : 1,
  "佘" : 1,
  "余" : 1,
  "佟" : 1,
  "侯" : 1,
  "俞" : 1,
  "倪" : 1,
  "傅" : 1,
  "储" : 1,
  "儲" : 1,
  "党" : 1,
  "关" : 1,
  "冀" : 1,
  "冉" : 1,
  "冯" : 1,
  "冷" : 1,
  "冼" : 1,
  "凌" : 1,
  "刁" : 1,
  "刑" : 1,
  "刘" : 1,
  "劉" : 1,
  "劳" : 1,
  "勞" : 1,
  "勾" : 1,
  "包" : 1,
  "匡" : 1,
  "区" : 1,
  "區" : 1,
  "华" : 1,
  "卓" : 1,
  "单" : 1,
  "卜" : 1,
  "卞" : 1,
  "卢" : 1,
  "卫" : 1,
  "印" : 1,
  "厉" : 1,
  "厲" : 1,
  "叢" : 1,
  "古" : 1,
  "台" : 1,
  "史" : 1,
  "叶" : 1,
  "司" : 1,
  "吉" : 1,
  "后" : 1,
  "向" : 1,
  "吕" : 1,
  "吳" : 1,
  "吴" : 1,
  "呂" : 1,
  "周" : 1,
  "哈" : 1,
  "唐" : 1,
  "商" : 1,
  "喬" : 1,
  "單" : 1,
  "喻" : 1,
  "嚴" : 1,
  "塗" : 1,
  "夏" : 1,
  "奚" : 1,
  "姚" : 1,
  "姜" : 1,
  "姬" : 1,
  "娄" : 1,
  "婁" : 1,
  "孔" : 1,
  "孙" : 1,
  "孟" : 1,
  "季" : 1,
  "孫" : 1,
  "宁" : 1,
  "安" : 1,
  "宋" : 1,
  "宓" : 1,
  "宗" : 1,
  "官" : 1,
  "宣" : 1,
  "宫" : 1,
  "宮" : 1,
  "容" : 1,
  "寇" : 1,
  "寧" : 1,
  "封" : 1,
  "尉" : 1,
  "尚" : 1,
  "尤" : 1,
  "尹" : 1,
  "屈" : 1,
  "展" : 1,
  "屠" : 1,
  "岑" : 1,
  "岳" : 1,
  "崔" : 1,
  "嵇" : 1,
  "左" : 1,
  "巩" : 1,
  "巫" : 1,
  "巴" : 1,
  "帅" : 1,
  "师" : 1,
  "帥" : 1,
  "師" : 1,
  "席" : 1,
  "常" : 1,
  "干" : 1,
  "庄" : 1,
  "应" : 1,
  "庞" : 1,
  "康" : 1,
  "庾" : 1,
  "廉" : 1,
  "廖" : 1,
  "延" : 1,
  "张" : 1,
  "張" : 1,
  "归" : 1,
  "彭" : 1,
  "徐" : 1,
  "忻" : 1,
  "慕" : 1,
  "應" : 1,
  "成" : 1,
  "戚" : 1,
  "戴" : 1,
  "房" : 1,
  "扈" : 1,
  "扶" : 1,
  "承" : 1,
  "支" : 1,
  "敖" : 1,
  "文" : 1,
  "斐" : 1,
  "方" : 1,
  "施" : 1,
  "旷" : 1,
  "易" : 1,
  "晁" : 1,
  "晉" : 1,
  "晋" : 1,
  "晏" : 1,
  "普" : 1,
  "曠" : 1,
  "曲" : 1,
  "曹" : 1,
  "曾" : 1,
  "朱" : 1,
  "朴" : 1,
  "权" : 1,
  "李" : 1,
  "杜" : 1,
  "杨" : 1,
  "杭" : 1,
  "林" : 1,
  "柏" : 1,
  "查" : 1,
  "柯" : 1,
  "柳" : 1,
  "柴" : 1,
  "栾" : 1,
  "桂" : 1,
  "桑" : 1,
  "梁" : 1,
  "梅" : 1,
  "楊" : 1,
  "楚" : 1,
  "楼" : 1,
  "榮" : 1,
  "樂" : 1,
  "樊" : 1,
  "樓" : 1,
  "欉" : 1,
  "權" : 1,
  "欒" : 1,
  "欧" : 1,
  "歐" : 1,
  "步" : 1,
  "武" : 1,
  "歸" : 1,
  "段" : 1,
  "殷" : 1,
  "毕" : 1,
  "毛" : 1,
  "汉" : 1,
  "江" : 1,
  "池" : 1,
  "汤" : 1,
  "汪" : 1,
  "沈" : 1,
  "沐" : 1,
  "沙" : 1,
  "洪" : 1,
  "浦" : 1,
  "涂" : 1,
  "淩" : 1,
  "温" : 1,
  "游" : 1,
  "湛" : 1,
  "湯" : 1,
  "溫" : 1,
  "滕" : 1,
  "满" : 1,
  "滿" : 1,
  "漆" : 1,
  "漢" : 1,
  "潘" : 1,
  "濮" : 1,
  "烏" : 1,
  "焦" : 1,
  "熊" : 1,
  "燕" : 1,
  "牛" : 1,
  "牟" : 1,
  "狄" : 1,
  "王" : 1,
  "班" : 1,
  "璩" : 1,
  "甄" : 1,
  "甘" : 1,
  "甯" : 1,
  "田" : 1,
  "申" : 1,
  "畢" : 1,
  "白" : 1,
  "皮" : 1,
  "盖" : 1,
  "盛" : 1,
  "盧" : 1,
  "瞿" : 1,
  "石" : 1,
  "祁" : 1,
  "祝" : 1,
  "禚" : 1,
  "禹" : 1,
  "秦" : 1,
  "程" : 1,
  "穆" : 1,
  "窦" : 1,
  "竇" : 1,
  "章" : 1,
  "童" : 1,
  "竺" : 1,
  "符" : 1,
  "简" : 1,
  "管" : 1,
  "簡" : 1,
  "米" : 1,
  "粘" : 1,
  "糜" : 1,
  "紀" : 1,
  "綦" : 1,
  "練" : 1,
  "繆" : 1,
  "纪" : 1,
  "练" : 1,
  "缪" : 1,
  "罗" : 1,
  "羅" : 1,
  "羊" : 1,
  "翁" : 1,
  "翟" : 1,
  "耿" : 1,
  "聂" : 1,
  "聞" : 1,
  "聶" : 1,
  "胡" : 1,
  "胥" : 1,
  "臧" : 1,
  "臺" : 1,
  "舒" : 1,
  "艾" : 1,
  "芮" : 1,
  "花" : 1,
  "苏" : 1,
  "苗" : 1,
  "苟" : 1,
  "范" : 1,
  "茅" : 1,
  "茆" : 1,
  "荀" : 1,
  "荆" : 1,
  "荊" : 1,
  "荣" : 1,
  "莊" : 1,
  "莫" : 1,
  "華" : 1,
  "萧" : 1,
  "萨" : 1,
  "萬" : 1,
  "葉" : 1,
  "葛" : 1,
  "董" : 1,
  "蒋" : 1,
  "蒙" : 1,
  "蒯" : 1,
  "蒲" : 1,
  "蓋" : 1,
  "蓝" : 1,
  "蔡" : 1,
  "蔣" : 1,
  "蔺" : 1,
  "蕭" : 1,
  "薛" : 1,
  "薩" : 1,
  "藍" : 1,
  "藺" : 1,
  "蘇" : 1,
  "虞" : 1,
  "衛" : 1,
  "袁" : 1,
  "裘" : 1,
  "裴" : 1,
  "褚" : 1,
  "覃" : 1,
  "解" : 1,
  "言" : 1,
  "計" : 1,
  "許" : 1,
  "詹" : 1,
  "談" : 1,
  "謝" : 1,
  "譙" : 1,
  "譚" : 1,
  "计" : 1,
  "许" : 1,
  "谈" : 1,
  "谢" : 1,
  "谭" : 1,
  "谯" : 1,
  "谷" : 1,
  "貝" : 1,
  "費" : 1,
  "賀" : 1,
  "賈" : 1,
  "賴" : 1,
  "贝" : 1,
  "费" : 1,
  "贺" : 1,
  "贾" : 1,
  "赖" : 1,
  "赫" : 1,
  "赵" : 1,
  "趙" : 1,
  "路" : 1,
  "車" : 1,
  "车" : 1,
  "辛" : 1,
  "辜" : 1,
  "边" : 1,
  "连" : 1,
  "逄" : 1,
  "連" : 1,
  "逯" : 1,
  "邊" : 1,
  "邓" : 1,
  "邝" : 1,
  "邢" : 1,
  "邬" : 1,
  "邰" : 1,
  "邱" : 1,
  "邴" : 1,
  "邵" : 1,
  "邹" : 1,
  "郁" : 1,
  "郎" : 1,
  "郑" : 1,
  "郜" : 1,
  "郝" : 1,
  "郦" : 1,
  "郭" : 1,
  "鄒" : 1,
  "鄔" : 1,
  "鄞" : 1,
  "鄢" : 1,
  "鄧" : 1,
  "鄭" : 1,
  "鄺" : 1,
  "酆" : 1,
  "酈" : 1,
  "释" : 1,
  "釋" : 1,
  "金" : 1,
  "鈕" : 1,
  "錡" : 1,
  "錢" : 1,
  "鍾" : 1,
  "鐘" : 1,
  "钟" : 1,
  "钮" : 1,
  "钱" : 1,
  "锺" : 1,
  "閔" : 1,
  "閩" : 1,
  "閻" : 1,
  "闕" : 1,
  "關" : 1,
  "闞" : 1,
  "闵" : 1,
  "闻" : 1,
  "闽" : 1,
  "阎" : 1,
  "阙" : 1,
  "阚" : 1,
  "阮" : 1,
  "阴" : 1,
  "陆" : 1,
  "陈" : 1,
  "陰" : 1,
  "陳" : 1,
  "陶" : 1,
  "陸" : 1,
  "隆" : 1,
  "隋" : 1,
  "隗" : 1,
  "雷" : 1,
  "霍" : 1,
  "靳" : 1,
  "鞏" : 1,
  "鞠" : 1,
  "韋" : 1,
  "韓" : 1,
  "韦" : 1,
  "韩" : 1,
  "項" : 1,
  "顏" : 1,
  "顧" : 1,
  "项" : 1,
  "顾" : 1,
  "颜" : 1,
  "饒" : 1,
  "饶" : 1,
  "馬" : 1,
  "馮" : 1,
  "駱" : 1,
  "马" : 1,
  "骆" : 1,
  "高" : 1,
  "魏" : 1,
  "魯" : 1,
  "鮑" : 1,
  "鲁" : 1,
  "鲍" : 1,
  "麥" : 1,
  "麦" : 1,
  "麻" : 1,
  "黃" : 1,
  "黄" : 1,
  "黎" : 1,
  "黨" : 1,
  "齊" : 1,
  "齐" : 1,
  "龍" : 1,
  "龐" : 1,
  "龔" : 1,
  "龙" : 1,
  "龚" : 1,
  "上官" : 1,
  "令狐" : 1,
  "司徒" : 1,
  "司馬" : 1,
  "司马" : 1,
  "尉迟" : 1,
  "尉遲" : 1,
  "张简" : 1,
  "張簡" : 1,
  "欧阳" : 1,
  "歐陽" : 1,
  "淳于" : 1,
  "澹台" : 1,
  "澹臺" : 1,
  "皇甫" : 1,
  "端木" : 1,
  "范姜" : 1,
  "赫连" : 1,
  "赫連" : 1,
}


class EastAsianExtractor(extractor.Extractor):
  def FileExtract(self, filename):
    """Since spacing has no significance in East Asian Languages, names
    may cross word boundaries, so this must be defined
    differently. But empty lines should be kept, since they would
    indicate things like paragraph boundaries.
    """
    fp = open(filename, 'r')
    nlines = []
    for line in fp.readlines():
      line = line.strip()
      if line == '': line = ' ' ## Keep empty line
      nlines.append(line)
    text = ''.join(nlines)
    for line in text.split():
      self.LineSegment(line)
    return self.tokens_


class ChineseExtractor(EastAsianExtractor):
  """Chinese extractor for foreign transcriptions.
  """

  def LineSegment(self, line):
    try: utext = unicode(line.strip(), 'utf-8')
    except TypeError: utext = line.strip()
    word = []
    for u in utext:
      c = u.encode('utf-8')
      if c in FOREIGN_CHARS_:
        word.append(u)
      else:
        if word:
          if len(word) >= MIN_LEN_:
            self.tokens_.append(tokens.Token(''.join(word)))
          word = []


class ChinesePersonalNameExtractor(EastAsianExtractor):
  """Extractor for potential Chinese Personal names. Takes the
  conservative approach that insists there be one or two characters
  after the potential family name. This will of course massively
  overgenerate.

  In the comments below "F" is a single-character family name, "G" is
  a single-character given name, and "FF" and "GG" are two-character
  equivalents. 
  """

  def LineSegment(self, line):
    try: utext = unicode(line.strip(), 'utf-8')
    except TypeError: utext = line.strip()
    for i in range(len(utext)):
      for k in [4, 3, 2]:
        sub = utext[i:i+k]
        if len(sub) != k: continue
        if k > 2 and sub[:2].encode('utf-8') in FAMILY_NAMES_:
          if not (Utils.script.HasDigit(sub) or Utils.script.HasPunctuation(sub)):
            self.tokens_.append(tokens.Token(sub))
        elif k < 4 and sub[:1].encode('utf-8') in FAMILY_NAMES_:
          if not Utils.script.HasDigit(sub):
            self.tokens_.append(tokens.Token(sub))
