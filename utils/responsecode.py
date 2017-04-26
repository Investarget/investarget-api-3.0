#coding=utf-8
responsecode = {
    '1000':'请求成功',
    '9999':'没标明状态码的错误',
    '8888':'数据来源不合法,datasource不匹配',
    '8889':'用户未登录',
    '8890':'give obj but expect queryset',


    '2001':'密码错误',
    '2002':'用户不存在',
    '2003':'登录类型不可用',
    '2004':'账号已存在',
    '2005':'验证码错误',
    '20051':'验证码过期',
    '2007':'mobile、email不能都为空',
    '20071':'请求参数有误',
    '20072':'参数缺失',


    '2009':'没有权限',
    '20091':'没有权限修改部分字段信息',
    '2010':'删除项有关联数据',

    '2011':'用户关系不存在',
    '2012':'用户关系已存在',
    '2013':'强关系只能有一个',
    '2014':'不能在两个相同的人之间建立关系',
    '2015':'建立关系的用户没有相应的权限(as_投资人或as_交易师)',

    '3000':'token验证失败',


    '4001':'上传项目信息有误',
    '4002':'项目不存在',
    '4003':'项目财务信息有误',
    '40031':'财务信息不再存在',
    '4004':'隐藏项目，没有权限查看',
    '4005':'项目收藏类型错误（没有该类型权限）',
    '4006':'项目收藏id不存在',

    '5001':'机构代码（orgcode）已存在',
    '5002':'机构不存在',

    '6001':'时间轴状态重复（不唯一），数据库数据有误',
    '6002':'时间轴不存在',
    '60021':'时间轴备注不存在',

}
