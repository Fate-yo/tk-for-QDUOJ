# -*- coding:utf-8 -*-
import json

dict = [
    {
        "model": "problem.problem",
        "pk": 1002,
        "fields": {
            "title": "入门训练 A+B问题",
            "description": r"<br />输入A、B，输出A+B。 <div class=\"sec_note\">说明：在&ldquo;问题描述&rdquo;这部分，会给出试题的意思，以及所要求的目标。 ",
            "input_description": r"输入描述:<br />输入的第一行包括两个整数，由空格分隔，分别表示A、B。 <div class=\"sec_note\"> <p>说明：&ldquo;输入格式&rdquo;是描述在测试你的程序时，所给的输入一定满足的格式。</p> <p>做题时你应该假设所给的输入是一定满足输入格式的要求的，所以你不需要对输入的格式进行检查。多余的格式检查可能会适得其反，使用你的程序错误。</p> <p>在测试的时候，系统会自动将输入数据输入到你的程序中，你不能给任何提示。比如，你在输入的时候提示&ldquo;请输入A、B&rdquo;之类的话是不需要的，这些多余的输出会使得你的程序被判定为错误。</p>   <br />输入样例: <br />12 45 <div class=\"sec_note\"> <p>说明：&ldquo;样例输入&rdquo;给出了一组满足&ldquo;输入格式&rdquo;要求的输入的例子。</p> <p>这里给出的输入只是可能用来测试你的程序的一个输入，在测试的时候，还会有更多的输入用来测试你的程序。</p>  ",
            "output_description": r"<br />输出描述: <br />输出一行，包括一个整数，表示A+B的值。 <div class=\"sec_note\"> <p>说明：&ldquo;输出格式&rdquo;是要求你的程序在输出结果的时候必须满足的格式。</p> <p>在输出时，你的程序必须满足这个格式的要求，不能少任何内容，也不能多任何内容。如果你的内容和输出格式要求的不一样，你的程序会被判断为错误，包括你输出了提示信息、中间调试信息、计时或者统计的信息等。</p>  <br /> 输出样例: <br />57 <div class=\"sec_note\"> <p>说明：&ldquo;样例输出&rdquo;给出了一组满足&ldquo;输出格式&rdquo;要求的输出的例子。</p> <p>样例输出中的结果是和样例输入中的是对应的，因此，你可以使用样例的输入输出简单的检查你的程序。</p> <p>要特别指出的是，能够通过样例输入输出的程序并不一定是正确的程序，在测试的时候，会用很多组数据进行测试，而不局限于样例数据。有可能一个程序通过了样例数据，但测试的时候仍只能得0分，可能因为这个程序只在一些类似样例的特例中正确，而不具有通用性，再测试更多数据时会出现错误。</p> <p>比如，对于本题，如果你写一个程序不管输入是什么都输入57，则样例数据是对的，但是测试其他数据，哪怕输入是1和2，这个程序也输出57，则对于其他数据这个程序都不正确。</p>  ",

            "test_case_id": "138521634",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />-10000 &lt;= A, B &lt;= 10000。 <div class=\"sec_note\"> <p>说明：&ldquo;数据规模与约定&rdquo;中给出了试题中主要参数的范围。</p> <p>这个范围对于解题非常重要，不同的数据范围会导致试题需要使用不同的解法来解决。比如本题中给的A、B范围不大，可以使用整型(int)来保存，如果范围更大，超过int的范围，则要考虑其他方法来保存大数。</p> <p>有一些范围在方便的时候是在&ldquo;问题描述&rdquo;中直接给的，所以在做题时不仅要看这个范围，还要注意问题描述。</p>  ",
            "create_time": "2017-12-28T03:15:44.3Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 1 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T1",
            "tags": [
                2
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1003,
        "fields": {
            "title": "入门训练 序列求和",
            "description": r"<br /> \t求1+2+3+...+n的值。 ",
            "input_description": r"输入描述:<br /> \t输入包括一个整数n。  <br />输入样例: <br /> \t4 ",
            "output_description": r"<br />输出描述: <br /> \t输出一行，包括一个整数，表示1+2+3+...+n的值。 <br /> 输出样例: <br /> \t10 ",

            "test_case_id": "257782451",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1 &lt;= n &lt;= 1,000,000,000。 \t<div class=\"sec_note\"> \t<p>说明：请注意这里的数据规模。</p> \t<p>本题直接的想法是直接使用一个循环来累加，然而，当数据规模很大时，这种“暴力”的方法往往会导致超时。此时你需要想想其他方法。你可以试一试，如果使用1000000000作为你的程序的输入，你的程序是不是能在规定的上面规定的时限内运行出来。</p> \t<p>本题另一个要值得注意的地方是答案的大小不在你的语言默认的整型(int)范围内，如果使用整型来保存结果，会导致结果错误。</p> \t<p>如果你使用C++或C语言而且准备使用printf输出结果，则你的格式字符串应该写成%I64d以输出long long类型的整数。</p> \t ",
            "create_time": "2017-12-28T03:15:44.4Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 2 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T2",
            "tags": [
                2
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1004,
        "fields": {
            "title": "入门训练 圆的面积",
            "description": r"<br /> \t给定圆的半径r，求圆的面积。 ",
            "input_description": r"输入描述:<br /> \t输入包含一个整数r，表示圆的半径。  <br />输入样例: <br /> \t4 ",
            "output_description": r"<br />输出描述: <br /> \t输出一行，包含一个实数，四舍五入保留小数点后7位，表示圆的面积。 \t<div class=\"sec_note\"> \t<p>说明：在本题中，输入是一个整数，但是输出是一个实数。</p> \t<p>对于实数输出的问题，请一定看清楚实数输出的要求，比如本题中要求保留小数点后7位，则你的程序必须<b>严格的</b>输出7位小数，输出过多或者过少的小数位数都是不行的，都会被认为错误。</p> \t<p>实数输出的问题如果没有特别说明，舍入都是按四舍五入进行。</p> \t <br /> 输出样例: <br /> \t50.2654825 ",

            "test_case_id": "377043268",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1 &lt;= r &lt;= 10000。 ",
            "create_time": "2017-12-28T03:15:44.5Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 3 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T3",
            "tags": [
                2
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1005,
        "fields": {
            "title": "入门训练 Fibonacci数列",
            "description": r"<br /> \t<p>Fibonacci数列的递推公式为：F<sub>n</sub>=F<sub>n-1</sub>+F<sub>n-2</sub>，其中F<sub>1</sub>=F<sub>2</sub>=1。</p> \t<p>当n比较大时，F<sub>n</sub>也非常大，现在我们想知道，F<sub>n</sub>除以10007的余数是多少。</p> ",
            "input_description": r"输入描述:<br /> \t输入包含一个整数n。 <br />输入样例: <br /> \t10",
            "output_description": r"<br />输出描述: <br /> \t输出一行，包含一个整数，表示F<sub>n</sub>除以10007的余数。 \t<div class=\"sec_note\"> \t<p>说明：在本题中，答案是要求F<sub>n</sub>除以10007的余数，因此我们只要能算出这个余数即可，而不需要先计算出F<sub>n</sub>的准确值，再将计算的结果除以10007取余数，直接计算余数往往比先算出原数再取余简单。</p> \t <br /> 输出样例: <br /> \t55",

            "test_case_id": "496304085",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1 &lt;= n &lt;= 1,000,000。",
            "create_time": "2017-12-28T03:15:44.6Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 4 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T4",
            "tags": [
                2
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1006,
        "fields": {
            "title": "基础练习 闰年判断",
            "description": r"<br /> \t<p>给定一个年份，判断这一年是不是闰年。</p> \t<p>当以下情况之一满足时，这一年是闰年：</p> \t<p>1. 年份是4的倍数而不是100的倍数；</p> \t<p>2. 年份是400的倍数。</p> \t<p>其他的年份都不是闰年。</p> ",
            "input_description": r"输入描述:<br /> \t输入包含一个整数y，表示当前的年份。 <br />输入样例: <br /> \t2013",
            "output_description": r"<br />输出描述: <br /> \t输出一行，如果给定的年份是闰年，则输出yes，否则输出no。 \t<div class=\"sec_note\"> \t<p>说明：当试题指定你输出一个字符串作为结果（比如本题的yes或者no，你需要严格按照试题中给定的大小写，写错大小写将不得分。 \t <br /> 输出样例: <br /> \tno",

            "test_case_id": "5115564902",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1990 &lt;= y &lt;= 2050。",
            "create_time": "2018-01-28T03:15:44.7Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 5 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T5",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1007,
        "fields": {
            "title": "基础练习 01字串",
            "description": r"<br /> \t<p>对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：</p> \t<p>00000</p> \t<p>00001</p> \t<p>00010</p> \t<p>00011</p> \t<p>00100</p> \t<p>请按从小到大的顺序输出这32种01串。</p> ",
            "input_description": r"输入描述:<br /> \t本试题没有输入。 <br />输入样例: <br /> \t00000<br /> \t00001<br /> \t00010<br /> \t00011<br /> \t&lt;以下部分省略&gt; \t",
            "output_description": r"<br />输出描述: <br /> \t输出32行，按从小到大的顺序每行一个长度为5的01串。 <br /> 输出样例: <br />",

            "test_case_id": "6134825719",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-01-28T03:15:44.8Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 6 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T6",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1008,
        "fields": {
            "title": "基础练习 字母图形",
            "description": r"<br /> <p>利用字母可以组成一些美丽的图形，下面给出了一个例子：</p> <p>ABCDEFG</p> <p>BABCDEF</p> <p>CBABCDE</p> <p>DCBABCD</p> <p>EDCBABC</p> <p>这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。</p> ",
            "input_description": r"输入描述:<br />输入一行，包含两个整数n和m，分别表示你要输出的图形的行数的列数。 <br />输入样例: <br />5 7",
            "output_description": r"<br />输出描述: <br />输出n行，每个m个字符，为你的图形。<br /> 输出样例: <br />ABCDEFG<br /> BABCDEF<br /> CBABCDE<br /> DCBABCD<br /> EDCBABC",

            "test_case_id": "7154086536",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />1 &lt;= n, m &lt;= 26。",
            "create_time": "2018-01-28T03:15:44.9Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 7 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T7",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1009,
        "fields": {
            "title": "基础练习 数列特征",
            "description": r"<br /> <p>给出n个数，找出这n个数的最大值，最小值，和。</p> ",
            "input_description": r"输入描述:<br /> <p>第一行为整数n，表示数的个数。</p> <p>第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。</p>  <br />输入样例: <br />5<br /> 1 3 -2 4 5",
            "output_description": r"<br />输出描述: <br />输出三行，每行一个整数。第一行表示这些数中的最大值，第二行表示这些数中的最小值，第三行表示这些数的和。<br /> 输出样例: <br />5<br /> -2<br /> 11",

            "test_case_id": "8173347353",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />1 &lt;= n &lt;= 10000。",
            "create_time": "2018-01-28T03:15:44.10Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 8 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T8",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1010,
        "fields": {
            "title": "基础练习 查找整数",
            "description": r"<br /> \t<p>给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行包含一个整数n。</p> \t<p>第二行包含n个非负整数，为给定的数列，数列中的每个数都不大于10000。</p> \t<p>第三行包含一个整数a，为待查找的数。</p> <br />输入样例: <br /> \t6<br /> \t1 9 4 8 3 9<br /> \t9 ",
            "output_description": r"<br />输出描述: <br /> \t如果a在数列中出现了，输出它第一次出现的位置(位置从1开始编号)，否则输出-1。 <br /> 输出样例: <br /> \t2 \t",

            "test_case_id": "9192608170",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1 &lt;= n &lt;= 1000。 ",
            "create_time": "2018-01-28T03:15:44.11Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 9 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T9",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1011,
        "fields": {
            "title": "基础练习 杨辉三角形",
            "description": r"<br /> \t<p>杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)<sup>i</sup>的展开式的系数。</p> 　　<p>它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。</p> 　　<p>下面给出了杨辉三角形的前4行：</p> 　　<p>&nbsp;&nbsp;&nbsp;1</p> 　　<p>&nbsp;&nbsp;1 1</p> 　　<p>&nbsp;1 2 1</p> 　　<p>1 3 3 1</p> 　　<p>给出n，输出它的前n行。</p> ",
            "input_description": r"输入描述:<br /> \t<p>输入包含一个数n。</p> <br />输入样例: <br /> \t4 ",
            "output_description": r"<br />输出描述: <br /> \t输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。 <br /> 输出样例: <br /> \t1<br /> 1 1<br /> 1 2 1<br /> 1 3 3 1 \t",

            "test_case_id": "10211868987",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t1 &lt;= n &lt;= 34。 ",
            "create_time": "2018-01-28T03:15:44.12Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 10 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T10",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1047,
        "fields": {
            "title": "基础练习 特殊的数字",
            "description": r"<br />　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。",
            "input_description": r"输入描述:<br />　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "46905258399",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.48Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 46 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T46",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1048,
        "fields": {
            "title": "基础练习 回文数",
            "description": r"<br />　　1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。",
            "input_description": r"输入描述:<br />　　按从小到大的顺序输出满足条件的四位十进制数。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "47924519216",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.49Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 47 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T47",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1049,
        "fields": {
            "title": "基础练习 特殊回文数",
            "description": r"<br />　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。<br /> 　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。",
            "input_description": r"输入描述:<br />　　输入一行，包含一个正整数n。 <br />输入样例: <br />52",
            "output_description": r"<br />输出描述: <br />　　按从小到大的顺序输出满足条件的整数，每个整数占一行。<br /> 输出样例: <br />899998<br /> 989989<br /> 998899",

            "test_case_id": "48943780033",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　1&lt;=n&lt;=54。",
            "create_time": "2018-01-28T03:15:44.50Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 48 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T48",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1050,
        "fields": {
            "title": "基础练习 十进制转十六进制",
            "description": r"<br />　　十六进制数是在程序设计时经常要使用到的一种整数的表示方式。它有0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F共16个符号，分别表示十进制数的0至15。十六进制的计数方法是满16进1，所以十进制数16在十六进制中是10，而十进制的17在十六进制中是11，以此类推，十进制的30在十六进制中是1E。<br /> 　　给出一个非负整数，将它表示成十六进制的形式。",
            "input_description": r"输入描述:<br />　　输入包含一个非负整数a，表示要转换的数。0&lt;=a&lt;=2147483647 <br />输入样例: <br />30",
            "output_description": r"<br />输出描述: <br />　　输出这个整数的16进制表示<br /> 输出样例: <br />1E",

            "test_case_id": "49963040850",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.51Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 49 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T49",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1051,
        "fields": {
            "title": "基础练习 十六进制转十进制",
            "description": r"<br />　　从键盘输入一个不超过8位的正的十六进制数字符串，将它转换为正的十进制数后输出。<br /> 　　注：十六进制数中的10~15分别用大写的英文字母A、B、C、D、E、F表示。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />FFFF",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />65535",

            "test_case_id": "50982301667",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.52Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 50 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T50",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1052,
        "fields": {
            "title": "基础练习 十六进制转八进制",
            "description": r"<br /><b>问题描述</b><b></b><br /> 　　给定n个十六进制正整数，输出它们对应的八进制数。<br /> <br /> <b>输入格式</b><b></b><br /> 　　输入的第一行为一个正整数n （1&lt;=n&lt;=10）。<br /> 　　接下来n行，每行一个由0~9、大写字母A~F组成的字符串，表示要转换的十六进制正整数，每个十六进制数长度不超过100000。<br /> <br /> <b>输出格式</b><b></b><br /> 　　输出n行，每行为输入对应的八进制正整数。<br /> <br /> 　　<b>【注意</b><b></b>】<br /> 　　输入的十六进制数不会有前导0，比如012A。<br /> 　　输出的八进制数也不能有前导0。<br /> <br /> <b>样例输入</b><b></b><br /> 　　2<br /> 　　39<br /> 　　123ABC<br /> <br /> <b>样例输出</b><b></b><br /> 　　71<br /> 　　4435274<br /> <br /> 　　<b><b>【</b>提示</b><b></b>】<br /> 　　先将十六进制数转换成某进制数，再由某进制数转换成八进制。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "511001562484",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.53Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 51 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T51",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1053,
        "fields": {
            "title": "基础练习 数列排序",
            "description": r"<br />　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1&lt;=n&lt;=200",
            "input_description": r"输入描述:<br />　　第一行为一个整数n。<br /> 　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。 <br />输入样例: <br />5<br /> 8 3 6 4 9",
            "output_description": r"<br />输出描述: <br />　　输出一行，按从小到大的顺序输出排序后的数列。<br /> 输出样例: <br />3 4 6 8 9",

            "test_case_id": "521020823301",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.54Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 52 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T52",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1055,
        "fields": {
            "title": "基础练习 时间转换",
            "description": r"<br />　　给定一个以秒为单位的时间t，要求用“&lt;H&gt;:&lt;M&gt;:&lt;S&gt;”的格式来表示这个时间。&lt;H&gt;表示时间，&lt;M&gt;表示分钟，而&lt;S&gt;表示秒，它们都是整数且没有前导的“0”。例如，若t=0，则应输出是“0:0:0”；若t=3661，则输出“1:1:1”。",
            "input_description": r"输入描述:<br />　　输入只有一行，是一个整数t（0&lt;=t&lt;=86399）。 <br />输入样例: <br />0",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，是以“&lt;H&gt;:&lt;M&gt;:&lt;S&gt;”的格式所表示的时间，不包括引号。<br /> 输出样例: <br />0:0:0",

            "test_case_id": "541059344935",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.56Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 54 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T54",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1057,
        "fields": {
            "title": "基础练习 字符串对比",
            "description": r"<br />　　给定两个仅由大写字母或小写字母组成的字符串(长度介于1到10之间)，它们之间的关系是以下4中情况之一：<br /> 　　1：两个字符串长度不等。比如 Beijing 和 Hebei<br /> 　　2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing<br /> 　　3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和        BEIjing<br /> 　　4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing<br /> 　　编程判断输入的两个字符串之间的关系属于这四类中的哪一类，给出所属的类的编号。",
            "input_description": r"输入描述:<br />　　包括两行，每行都是一个字符串 <br />输入样例: <br />BEIjing<pre class='pddata'> <font face=\"Times New Roman\" size=\"3\">beiJing </font> </pre> ",
            "output_description": r"<br />输出描述: <br />　　仅有一个数字，表明这两个字符串的关系编号<br /> 输出样例: <br />3",

            "test_case_id": "561097866569",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.58Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 56 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T56",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1058,
        "fields": {
            "title": "基础练习 分解质因数",
            "description": r"<br />　　求出区间[a,b]中所有整数的质因数分解。",
            "input_description": r"输入描述:<br />　　输入两个整数a，b。 <br />输入样例: <br />3 10",
            "output_description": r"<br />输出描述: <br />　　每行输出一个数的分解，形如k=a1*a2*a3...(a1&lt;=a2&lt;=a3...，k也是从小到大的)(具体可看样例)<br /> 输出样例: <br />3=3<br /> 4=2*2<br /> 5=5<br /> 6=2*3<br /> 7=7<br /> 8=2*2*2<br /> 9=3*3<br /> 10=2*5",

            "test_case_id": "571117127386",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　先筛出所有素数，然后再分解。",
            "create_time": "2018-01-28T03:15:44.59Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 57 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T57",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1059,
        "fields": {
            "title": "基础练习 矩阵乘法",
            "description": r"<br />　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）<br /> 　　例如：<br /> 　　A =<br /> 　　1 2<br /> 　　3 4<br /> 　　A的2次幂<br /> 　　7 10<br /> 　　15 22",
            "input_description": r"输入描述:<br />　　第一行是一个正整数N、M（1&lt;=N&lt;=30, 0&lt;=M&lt;=5），表示矩阵A的阶数和要求的幂数<br /> 　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值 <br />输入样例: <br />2 2<br /> 1 2<br /> 3 4",
            "output_description": r"<br />输出描述: <br />　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开<br /> 输出样例: <br />7 10<br /> 15 22",

            "test_case_id": "581136388203",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.60Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 58 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T58",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1060,
        "fields": {
            "title": "基础练习 矩形面积交",
            "description": r"<br />　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。",
            "input_description": r"输入描述:<br />　　输入仅包含两行，每行描述一个矩形。<br /> 　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。 <br />输入样例: <br />1 1 3 3<br /> 2 2 4 4",
            "output_description": r"<br />输出描述: <br />　　输出仅包含一个实数，为交的面积，保留到小数后两位。<br /> 输出样例: <br />1.00",

            "test_case_id": "591155649020",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.61Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 59 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T59",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1061,
        "fields": {
            "title": "基础练习 完美的代价",
            "description": r"<br />　　回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，请你计算最少的交换次数使得该串变成一个完美的回文串。<br /> 　　交换的定义是：交换两个相邻的字符<br /> 　　例如mamad<br /> 　　第一次交换 ad : mamda<br /> 　　第二次交换 md : madma<br /> 　　第三次交换 ma : madam (回文！完美！)",
            "input_description": r"输入描述:<br />　　第一行是一个整数N，表示接下来的字符串的长度(N &lt;= 8000)<br /> 　　第二行是一个字符串，长度为N.只包含小写字母 <br />输入样例: <br />5<br /> mamad",
            "output_description": r"<br />输出描述: <br />　　如果可能，输出最少的交换次数。<br /> 　　否则输出Impossible<br /> 输出样例: <br />3",

            "test_case_id": "601174909837",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.62Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 60 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T60",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1062,
        "fields": {
            "title": "基础练习 数的读法",
            "description": r"<br />　　Tom教授正在给研究生讲授一门关于基因的课程，有一件事情让他颇为头疼：一条染色体上有成千上万个碱基对，它们从0开始编号，到几百万，几千万，甚至上亿。<br /> 　　比如说，在对学生讲解第1234567009号位置上的碱基时，光看着数字是很难准确的念出来的。<br /> 　　所以，他迫切地需要一个系统，然后当他输入12 3456 7009时，会给出相应的念法：<br /> 　　十二亿三千四百五十六万七千零九<br /> 　　用汉语拼音表示为<br /> 　　shi er yi san qian si bai wu shi liu wan qi qian ling jiu<br /> 　　这样他只需要照着念就可以了。<br /> 　　你的任务是帮他设计这样一个系统：给定一个阿拉伯数字串，你帮他按照中文读写的规范转为汉语拼音字串，相邻的两个音节用一个空格符格开。<br /> 　　注意必须严格按照规范，比如说“10010”读作“yi wan ling yi shi”而不是“yi wan ling shi”，“100000”读作“shi wan”而不是“yi shi wan”，“2000”读作“er qian”而不是“liang qian”。",
            "input_description": r"输入描述:<br />　　有一个数字串，数值大小不超过2,000,000,000。 <br />输入样例: <br />1234567009",
            "output_description": r"<br />输出描述: <br />　　是一个由小写英文字母，逗号和空格组成的字符串，表示该数的英文读法。<br /> 输出样例: <br />shi er yi san qian si bai wu shi liu wan qi qian ling jiu",

            "test_case_id": "611194170654",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.63Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 61 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T61",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1063,
        "fields": {
            "title": "基础练习 Sine之舞",
            "description": r"<br />　　最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。<br /> 　　不妨设<br /> 　　An=sin(1–sin(2+sin(3–sin(4+...sin(n))...)<br /> 　　Sn=(...(A1+n)A2+n-1)A3+...+2)An+1<br /> 　　FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。",
            "input_description": r"输入描述:<br />　　仅有一个数：N&lt;201。 <br />输入样例: <br />3",
            "output_description": r"<br />输出描述: <br />　　请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。<br /> 输出样例: <br />((sin(1)+3)sin(1–sin(2))+2)sin(1–sin(2+sin(3)))+1",

            "test_case_id": "621213431471",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.64Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 62 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T62",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1064,
        "fields": {
            "title": "基础练习 FJ的字符串",
            "description": r"<br />　　FJ在沙盘上写了这样一些字符串：<br /> 　　A1 = “A”<br /> 　　A2 = “ABA”<br /> 　　A3 = “ABACABA”<br /> 　　A4 = “ABACABADABACABA”<br /> 　　… …<br /> 　　你能找出其中的规律并写所有的数列AN吗？",
            "input_description": r"输入描述:<br />　　仅有一个数：N ≤ 26。 <br />输入样例: <br />3",
            "output_description": r"<br />输出描述: <br />　　请输出相应的字符串AN，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。<br /> 输出样例: <br />ABACABA",

            "test_case_id": "631232692288",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.65Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 63 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T63",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1065,
        "fields": {
            "title": "基础练习 芯片测试",
            "description": r"<br />　　有n（2≤n≤20）块芯片，有好有坏，已知好芯片比坏芯片多。<br /> 　　每个芯片都能用来测试其他芯片。用好芯片测试其他芯片时，能正确给出被测试芯片是好还是坏。而用坏芯片测试其他芯片时，会随机给出好或是坏的测试结果（即此结果与被测试芯片实际的好坏无关）。<br /> 　　给出所有芯片的测试结果，问哪些芯片是好芯片。",
            "input_description": r"输入描述:<br />　　输入数据第一行为一个整数n，表示芯片个数。<br /> 　　第二行到第n+1行为n*n的一张表，每行n个数据。表中的每个数据为0或1，在这n行中的第i行第j列（1≤i, j≤n）的数据表示用第i块芯片测试第j块芯片时得到的测试结果，1表示好，0表示坏，i=j时一律为1（并不表示该芯片对本身的测试结果。芯片不能对本身进行测试）。 <br />输入样例: <br />3<br /> 1 0 1<br /> 0 1 0<br /> 1 0 1",
            "output_description": r"<br />输出描述: <br />　　按从小到大的顺序输出所有好芯片的编号<br /> 输出样例: <br />1 3",

            "test_case_id": "641251953105",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.66Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 64 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T64",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1066,
        "fields": {
            "title": "基础练习 龟兔赛跑预测",
            "description": r"<br />　　话说这个世界上有各种各样的兔子和乌龟，但是研究发现，所有的兔子和乌龟都有一个共同的特点——喜欢赛跑。于是世界上各个角落都不断在发生着乌龟和兔子的比赛，小华对此很感兴趣，于是决定研究不同兔子和乌龟的赛跑。他发现，兔子虽然跑比乌龟快，但它们有众所周知的毛病——骄傲且懒惰，于是在与乌龟的比赛中，一旦任一秒结束后兔子发现自己领先t米或以上，它们就会停下来休息s秒。对于不同的兔子，t，s的数值是不同的，但是所有的乌龟却是一致——它们不到终点决不停止。<br /> 　　然而有些比赛相当漫长，全程观看会耗费大量时间，而小华发现只要在每场比赛开始后记录下兔子和乌龟的数据——兔子的速度v1（表示每秒兔子能跑v1米），乌龟的速度v2，以及兔子对应的t，s值，以及赛道的长度l——就能预测出比赛的结果。但是小华很懒，不想通过手工计算推测出比赛的结果，于是他找到了你——清华大学计算机系的高才生——请求帮助，请你写一个程序，对于输入的一场比赛的数据v1，v2，t，s，l，预测该场比赛的结果。",
            "input_description": r"输入描述:<br />　　输入只有一行，包含用空格隔开的五个正整数v1，v2，t，s，l，其中(v1,v2&lt;=100;t&lt;=300;s&lt;=10;l&lt;=10000且为v1,v2的公倍数) <br />输入样例: <br />10 5 5 2 20",
            "output_description": r"<br />输出描述: <br />　　输出包含两行，第一行输出比赛结果——一个大写字母“T”或“R”或“D”，分别表示乌龟获胜，兔子获胜，或者两者同时到达终点。<br /> 　　第二行输出一个正整数，表示获胜者（或者双方同时）到达终点所耗费的时间（秒数）。<br /> 输出样例: <br />D<br /> 4",

            "test_case_id": "651271213922",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.67Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 65 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T65",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1067,
        "fields": {
            "title": "基础练习 回形取数",
            "description": r"<br />　　回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。",
            "input_description": r"输入描述:<br />　　输入第一行是两个不超过200的正整数m, n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。 <br />输入样例: <br />3 3<br /> 1 2 3<br /> 4 5 6<br /> 7 8 9",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。<br /> 输出样例: <br />1 4 7 8 9 6 3 2 5",

            "test_case_id": "661290474739",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.68Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 66 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T66",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1068,
        "fields": {
            "title": "基础练习 报时助手",
            "description": r"<br />　　给定当前的时间，请用英文的读法将它读出来。<br /> 　　时间用时h和分m表示，在英文的读法中，读一个时间的方法是：<br /> 　　如果m为0，则将时读出来，然后加上“o'clock”，如3:00读作“three o'clock”。<br /> 　　如果m不为0，则将时读出来，然后将分读出来，如5:30读作“five thirty”。<br /> 　　时和分的读法使用的是英文数字的读法，其中0~20读作：<br /> 　　0:zero, 1: one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten, 11:eleven, 12:twelve, 13:thirteen, 14:fourteen, 15:fifteen, 16:sixteen, 17:seventeen, 18:eighteen, 19:nineteen, 20:twenty。<br /> 　　30读作thirty，40读作forty，50读作fifty。<br /> 　　对于大于20小于60的数字，首先读整十的数，然后再加上个位数。如31首先读30再加1的读法，读作“thirty one”。<br /> 　　按上面的规则21:54读作“twenty one fifty four”，9:07读作“nine seven”，0:15读作“zero fifteen”。",
            "input_description": r"输入描述:<br />　　输入包含两个非负整数h和m，表示时间的时和分。非零的数字前没有前导0。h小于24，m小于60。 <br />输入样例: <br />0 15",
            "output_description": r"<br />输出描述: <br />　　输出时间时刻的英文。<br /> 输出样例: <br />zero fifteen",

            "test_case_id": "671309735556",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.69Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 67 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T67",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1069,
        "fields": {
            "title": "基础练习 2n皇后问题",
            "description": r"<br />　　给定一个n*n的棋盘，棋盘中有一些位置不能放皇后。现在要向棋盘中放入n个黑皇后和n个白皇后，使任意的两个黑皇后都不在同一行、同一列或同一条对角线上，任意的两个白皇后都不在同一行、同一列或同一条对角线上。问总共有多少种放法？n小于等于8。",
            "input_description": r"输入描述:<br />　　输入的第一行为一个整数n，表示棋盘的大小。<br /> 　　接下来n行，每行n个0或1的整数，如果一个整数为1，表示对应的位置可以放皇后，如果一个整数为0，表示对应的位置不可以放皇后。 <br />输入样例: <br />4<br /> 1 1 1 1<br /> 1 1 1 1<br /> 1 1 1 1<br /> 1 1 1 1",
            "output_description": r"<br />输出描述: <br />　　输出一个整数，表示总共有多少种放法。<br /> 输出样例: <br />2",

            "test_case_id": "681328996373",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.70Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 68 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T68",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1070,
        "fields": {
            "title": "基础练习 Huffuman树",
            "description": r"<br />　　Huffman树在编码中有着广泛的应用。在这里，我们只关心Huffman树的构造过程。<br /> 　　给出一列数{<i>p<sub>i</sub></i>}={<i>p</i><sub>0</sub>, <i>p</i><sub>1</sub>, …, <i>p<sub>n</sub></i><sub>-1</sub>}，用这列数构造Huffman树的过程如下：<br /> 　　1.      找到{<i>p<sub>i</sub></i>}中最小的两个数，设为<i>p<sub>a</sub></i>和<i>p<sub>b</sub></i>，将<i>p<sub>a</sub></i>和<i>p<sub>b</sub></i>从{<i>p<sub>i</sub></i>}中删除掉，然后将它们的和加入到{<i>p<sub>i</sub></i>}中。这个过程的费用记为<i>p<sub>a</sub></i> + <i>p<sub>b</sub></i>。<br /> 　　2.      重复步骤1，直到{<i>p<sub>i</sub></i>}中只剩下一个数。<br /> 　　在上面的操作过程中，把所有的费用相加，就得到了构造Huffman树的总费用。<br /> 　　本题任务：对于给定的一个数列，现在请你求出用该数列构造Huffman树的总费用。<br /> <br /> 　　例如，对于数列{<i>p<sub>i</sub></i>}={5, 3, 8, 2, 9}，Huffman树的构造过程如下：<br /> 　　1.      找到{5, 3, 8, 2, 9}中最小的两个数，分别是2和3，从{<i>p<sub>i</sub></i>}中删除它们并将和5加入，得到{5, 8, 9, 5}，费用为5。<br /> 　　2.      找到{5, 8, 9, 5}中最小的两个数，分别是5和5，从{<i>p<sub>i</sub></i>}中删除它们并将和10加入，得到{8, 9, 10}，费用为10。<br /> 　　3.      找到{8, 9, 10}中最小的两个数，分别是8和9，从{<i>p<sub>i</sub></i>}中删除它们并将和17加入，得到{10, 17}，费用为17。<br /> 　　4.      找到{10, 17}中最小的两个数，分别是10和17，从{<i>p<sub>i</sub></i>}中删除它们并将和27加入，得到{27}，费用为27。<br /> 　　5.      现在，数列中只剩下一个数27，构造过程结束，总费用为5+10+17+27=59。",
            "input_description": r"输入描述:<br />　　输入的第一行包含一个正整数<i>n</i>（<i>n</i>&lt;=100）。<br /> 　　接下来是<i>n</i>个正整数，表示<i>p</i><sub>0</sub>, <i>p</i><sub>1</sub>, …, <i>p<sub>n</sub></i><sub>-1</sub>，每个数不超过1000。 <br />输入样例: <br />5<br /> 5 3 8 2 9",
            "output_description": r"<br />输出描述: <br />　　输出用这些数构造Huffman树的总费用。<br /> 输出样例: <br />59",

            "test_case_id": "691348257190",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-01-28T03:15:44.71Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 69 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T69",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1071,
        "fields": {
            "title": "基础练习 高精度加法",
            "description": r"<br />　　输入两个整数<i>a</i>和<i>b</i>，输出这两个整数的和。<i>a</i>和<i>b</i>都不超过100位。",
            "input_description": r"输入描述:<br />　　由于<i>a</i>和<i>b</i>都比较大，所以不能直接使用语言中的标准数据类型来存储。对于这种问题，一般使用数组来处理。<br /> 　　定义一个数组<i>A</i>，<i>A</i>[0]用于存储<i>a</i>的个位，<i>A</i>[1]用于存储<i>a</i>的十位，依此类推。同样可以用一个数组<i>B</i>来存储<i>b</i>。<br /> 　　计算<i>c</i> = <i>a</i> + <i>b</i>的时候，首先将<i>A</i>[0]与<i>B</i>[0]相加，如果有进位产生，则把进位（即和的十位数）存入<i>r</i>，把和的个位数存入<i>C</i>[0]，即<i>C</i>[0]等于(<i>A</i>[0]+<i>B</i>[0])%10。然后计算<i>A</i>[1]与<i>B</i>[1]相加，这时还应将低位进上来的值<i>r</i>也加起来，即<i>C</i>[1]应该是<i>A</i>[1]、<i>B</i>[1]和<i>r</i>三个数的和．如果又有进位产生，则仍可将新的进位存入到<i>r</i>中，和的个位存到<i>C</i>[1]中。依此类推，即可求出<i>C</i>的所有位。<br /> 　　最后将<i>C</i>输出即可。 <br />输入样例: <br />20100122201001221234567890<br /> 2010012220100122",
            "output_description": r"<br />输出描述: <br />　　输入包括两行，第一行为一个非负整数<i>a</i>，第二行为一个非负整数<i>b</i>。两个整数都不超过100位，两数的最高位都不是0。<br /> 输出样例: <br />20100122203011233454668012",

            "test_case_id": "701367518007",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　输出一行，表示<i>a </i>+ <i>b</i>的值。",
            "create_time": "2018-01-28T03:15:44.72Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 70 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T70",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1072,
        "fields": {
            "title": "基础练习 阶乘计算",
            "description": r"<br />　　输入一个正整数<i>n</i>，输出<i>n</i>!的值。<br /> 　　其中<i>n</i>!=1*2*3*…*<i>n</i>。",
            "input_description": r"输入描述:<br />　　<i>n</i>!可能很大，而计算机能表示的整数范围有限，需要使用高精度计算的方法。使用一个数组<i>A</i>来表示一个大整数<i>a</i>，<i>A</i>[0]表示<i>a</i>的个位，<i>A</i>[1]表示<i>a</i>的十位，依次类推。<br /> 　　将<i>a</i>乘以一个整数<i>k</i>变为将数组<i>A</i>的每一个元素都乘以<i>k</i>，请注意处理相应的进位。<br /> 　　首先将<i>a</i>设为1，然后乘2，乘3，当乘到<i>n</i>时，即得到了<i>n</i>!的值。 <br />输入样例: <br />10",
            "output_description": r"<br />输出描述: <br />　　输入包含一个正整数<i>n</i>，<i>n</i>&lt;=1000。<br /> 输出样例: <br />3628800",

            "test_case_id": "711386778824",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　输出<i>n</i>!的准确值。",
            "create_time": "2018-01-28T03:15:44.73Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 1,
            "source": r"蓝桥杯练习系统 ID: 71 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T71",
            "tags": [
                3
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1012,
        "fields": {
            "title": "算法训练 区间k大数查询",
            "description": r"<br /> \t<p>给定一个序列，每次询问序列中第l个数到第r个数中第K大的数是哪个。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行包含一个数n，表示序列长度。</p> \t<p>第二行包含n个正整数，表示给定的序列。</p> \t<p>第三个包含一个正整数m，表示询问个数。</p> <p>接下来m行，每行三个数l,r,K，表示询问序列从左往右第l个数到第r个数中，从大往小第K大的数是哪个。序列元素从1开始标号。</p>  <br />输入样例: <br /> 5<br /> 1 2 3 4 5<br /> 2<br /> 1 5 2<br /> 2 3 2 ",
            "output_description": r"<br />输出描述: <br /> \t总共输出m行，每行一个数，表示询问的答案。 <br /> 输出样例: <br /> 4<br /> 2 \t",

            "test_case_id": "11231129804",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于30%的数据，n,m&lt;=100；</p> <p>对于100%的数据，n,m&lt;=1000；</p> <p>保证k&lt;=(r-l+1)，序列中的数&lt;=10<sup>6</sup>。</p> ",
            "create_time": "2018-02-28T03:15:44.13Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 11 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T11",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1013,
        "fields": {
            "title": "算法训练 最大最小公倍数",
            "description": r"<br /> <p>已知一个正整数N，问从1~N中任选出三个数，他们的最小公倍数最大可以为多少。</p> ",
            "input_description": r"输入描述:<br /> <p>输入一个正整数N。</p>  <br />输入样例: <br />9",
            "output_description": r"<br />输出描述: <br />输出一个整数，表示你找到的最小公倍数。<br /> 输出样例: <br />504",

            "test_case_id": "12250390621",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>1 &lt;= N &lt;= 10<sup>6</sup>。</p> ",
            "create_time": "2018-02-28T03:15:44.14Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 12 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T12",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1014,
        "fields": {
            "title": "算法训练 K好数",
            "description": r"<br /> \t<p>如果一个自然数N的K进制表示中任意的相邻的两位都不是相邻的数字，那么我们就说这个数是K好数。求L位K进制数中K好数的数目。例如K = 4，L = 2的时候，所有K好数为11、13、20、22、30、31、33 共7个。由于这个数目很大，请你输出它对1000000007取模后的值。</p> ",
            "input_description": r"输入描述:<br /> \t<p>输入包含两个正整数，K和L。</p>  <br />输入样例: <br /> 4 2 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数，表示答案对1000000007取模后的值。 <br /> 输出样例: <br /> 7 \t",

            "test_case_id": "13269651438",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于30%的数据，K<sup>L</sup> &lt;= 10<sup>6</sup>；</p> <p>对于50%的数据，K &lt;= 16， L &lt;= 10；</p> <p>对于100%的数据，1 &lt;= K,L &lt;= 100。</p> ",
            "create_time": "2018-02-28T03:15:44.15Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 13 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T13",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1015,
        "fields": {
            "title": "算法训练 结点选择",
            "description": r"<br /> \t<p>有一棵 n 个节点的树，树上每个节点都有一个正整数权值。如果一个点被选择了，那么在树上和它相邻的点都不能被选择。求选出的点的权值和最大是多少？</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行包含一个整数 n 。</p> \t<p>接下来的一行包含 n 个正整数，第 i 个正整数代表点 i 的权值。</p> \t<p>接下来一共 n-1 行，每行描述树上的一条边。</p>  <br />输入样例: <br /> 5<br /> 1 2 3 4 5<br /> 1 2<br /> 1 3<br /> 2 4<br /> 2 5 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数，代表选出的点的权值和的最大值。 <br /> 输出样例: <br /> 12 \t",

            "test_case_id": "14288912255",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> 选择3、4、5号点，权值和为 3+4+5 = 12 。 ",
            "create_time": "2018-02-28T03:15:44.16Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 14 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T14",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1016,
        "fields": {
            "title": "算法训练 最短路",
            "description": r"<br /> \t<p>给定一个n个顶点，m条边的有向图（其中某些边权可能为负，但保证没有负环）。请你计算从1号点到其他点的最短路（顶点从1到n编号）。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行两个整数n, m。</p> \t<p>接下来的m行，每行有三个整数u, v, l，表示u到v有一条长度为l的边。</p>  <br />输入样例: <br /> 3 3<br /> 1 2 -1<br /> 2 3 -1<br /> 3 1 2\t  ",
            "output_description": r"<br />输出描述: <br /> \t共n-1行，第i行表示1号点到i+1号点的最短路。 <br /> 输出样例: <br /> -1<br /> -2  \t",

            "test_case_id": "15308173072",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于10%的数据，n = 2，m = 2。</p> <p>对于30%的数据，n &lt;= 5，m &lt;= 10。</p> <p>对于100%的数据，1 &lt;= n &lt;= 20000，1 &lt;= m &lt;= 200000，-10000 &lt;= l &lt;= 10000，保证从任意顶点都能到达其他所有顶点。</p> ",
            "create_time": "2018-02-28T03:15:44.17Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 15 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T15",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1017,
        "fields": {
            "title": "算法训练 安慰奶牛",
            "description": r"<br /> \t<p>Farmer John变得非常懒，他不想再继续维护供奶牛之间供通行的道路。道路被用来连接N个牧场，牧场被连续地编号为1到N。每一个牧场都是一个奶牛的家。FJ计划除去P条道路中尽可能多的道路，但是还要保持牧场之间 的连通性。你首先要决定那些道路是需要保留的N-1条道路。第j条双向道路连接了牧场S<sub>j</sub>和E<sub>j</sub>(1 &lt;= S<sub>j</sub> &lt;= N; 1 &lt;= E<sub>j</sub> &lt;= N; S<sub>j</sub> != E<sub>j</sub>)，而且走完它需要L<sub>j</sub>的时间。没有两个牧场是被一条以上的道路所连接。奶牛们非常伤心，因为她们的交通系统被削减了。你需要到每一个奶牛的住处去安慰她们。每次你到达第i个牧场的时候(即使你已经到过)，你必须花去C<sub>i</sub>的时间和奶牛交谈。你每个晚上都会在同一个牧场(这是供你选择的)过夜，直到奶牛们都从悲伤中缓过神来。在早上 起来和晚上回去睡觉的时候，你都需要和在你睡觉的牧场的奶牛交谈一次。这样你才能完成你的 交谈任务。假设Farmer John采纳了你的建议，请计算出使所有奶牛都被安慰的最少时间。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第1行包含两个整数N和P。</p> \t<p>接下来N行，每行包含一个整数C<sub>i</sub>。</p> \t<p>接下来P行，每行包含三个整数S<sub>j</sub>, E<sub>j</sub>和L<sub>j</sub>。</p>  <br />输入样例: <br /> 5 7<br /> 10<br /> 10<br /> 20<br /> 6<br /> 30<br /> 1 2 5<br /> 2 3 5<br /> 2 4 12<br /> 3 4 17<br /> 2 5 15<br /> 3 5 6 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数, 所需要的总时间(包含和在你所在的牧场的奶牛的两次谈话时间)。 <br /> 输出样例: <br /> 176 \t",

            "test_case_id": "16327433889",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>5 &lt;= N &lt;= 10000，N-1 &lt;= P &lt;= 100000，0 &lt;= L<sub>j</sub> &lt;= 1000，1 &lt;= C<sub>i</sub> &lt;= 1,000。</p> ",
            "create_time": "2018-02-28T03:15:44.18Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 16 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T16",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1018,
        "fields": {
            "title": "算法训练 逆序对",
            "description": r"<br /> <p>Alice是一个让人非常愉跃的人!他总是去学习一些他不懂的问题，然后再想出许多稀奇古怪的题目。这几天，Alice又沉浸在逆序对的快乐当中，他已近学会了如何求逆序对对数，动态维护逆序对对数等等题目，他认为把这些题让你做简直是太没追求了，于是，经过一天的思考和完善，Alice终于拿出了一道他认为差不多的题目：</p> <p>有一颗2n-1个节点的二叉树，它有恰好n个叶子节点，每个节点上写了一个整数。如果将这棵树的所有叶子节点上的数从左到右写下来，便得到一个序列a[1]…a[n]。现在想让这个序列中的逆序对数量最少，但唯一的操作就是选树上一个非叶子节点，将它的左右两颗子树交换。他可以做任意多次这个操作。求在最优方案下，该序列的逆序对数最少有多少。</p> <p>Alice自己已近想出了题目的正解，他打算拿来和你分享，他要求你在最短的时间内完成。</p> ",
            "input_description": r"输入描述:<br /> <p>第一行一个整数n。</p> <p>下面每行，一个数x。</p> <p>如果x=0，表示这个节点非叶子节点，递归地向下读入其左孩子和右孩子的信息，如果x≠0，表示这个节点是叶子节点，权值为x。</p>  <br />输入样例: <br /> 3<br /> 0<br /> 0<br /> 3<br /> 1<br /> 2 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数，表示最少有多少逆序对。 <br /> 输出样例: <br /> 1 \t",

            "test_case_id": "17346694706",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于20%的数据，n &lt;= 5000。</p> <p>对于100%的数据，1 &lt;= n &lt;= 200000，0 &lt;= a[i]&lt;2^31。</p> ",
            "create_time": "2018-02-28T03:15:44.19Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 17 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T17",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1019,
        "fields": {
            "title": "算法训练 操作格子",
            "description": r"<br /> \t<p>有n个格子，从左到右放成一排，编号为1-n。</p> \t<p>共有m次操作，有3种操作类型：</p> \t<p>1.修改一个格子的权值，</p> \t<p>2.求连续一段格子权值和，</p> \t<p>3.求连续一段格子的最大值。</p> \t<p>对于每个2、3操作输出你所求出的结果。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行2个整数n，m。</p> \t<p>接下来一行n个整数表示n个格子的初始权值。</p> \t<p>接下来m行，每行3个整数p,x,y，p表示操作类型，p=1时表示修改格子x的权值为y，p=2时表示求区间[x,y]内格子权值和，p=3时表示求区间[x,y]内格子最大的权值。</p>  <br />输入样例: <br /> 4 3<br /> 1 2 3 4<br /> 2 1 3<br /> 1 4 3<br /> 3 1 4 ",
            "output_description": r"<br />输出描述: <br /> \t<p>有若干行，行数等于p=2或3的操作总数。</p> \t<p>每行1个整数，对应了每个p=2或3操作的结果。</p> <br /> 输出样例: <br /> 6<br /> 3 \t",

            "test_case_id": "18365955523",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t<p>对于20%的数据n &lt;= 100，m &lt;= 200。</p> \t<p>对于50%的数据n &lt;= 5000，m &lt;= 5000。</p> \t<p>对于100%的数据1 &lt;= n &lt;= 100000，m &lt;= 100000，0 &lt;= 格子权值 &lt;= 10000。</p> ",
            "create_time": "2018-02-28T03:15:44.20Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 18 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T18",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1045,
        "fields": {
            "title": "算法训练 摆动序列",
            "description": r"<br />　　如果一个序列满足下面的性质，我们就将它称为摆动序列：<br /> 　　1.        序列中的所有数都是不大于<i>k</i>的正整数；<br /> 　　2.        序列中至少有两个数。<br /> 　　3.        序列中的数两两不相等；<br /> 　　4.        如果第<i>i</i> – 1个数比第<i>i</i> – 2个数大，则第<i>i</i>个数比第<i>i</i> – 2个数小；如果第<i>i</i> – 1个数比第<i>i</i> – 2个数小，则第<i>i</i>个数比第<i>i</i> – 2个数大。<br /> 　　比如，当<i>k</i> = 3时，有下面几个这样的序列：<br /> 　　1 2<br /> 　　1 3<br /> 　　2 1<br /> 　　2 1 3<br /> 　　2 3<br /> 　　2 3 1<br /> 　　3 1<br /> 　　3 2<br /> 　　一共有8种，给定<i>k</i>，请求出满足上面要求的序列的个数。",
            "input_description": r"输入描述:<br />　　输入包含了一个整数<i>k</i>。（<i>k</i>&lt;=20） <br />输入样例: <br />3",
            "output_description": r"<br />输出描述: <br />　　输出一个整数，表示满足要求的序列个数。<br /> 输出样例: <br />8",

            "test_case_id": "44866736765",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.46Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 44 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T44",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1054,
        "fields": {
            "title": "算法训练 集合运算",
            "description": r"<br />　　给出两个整数集合A、B，求出他们的交集、并集以及B在A中的余集。",
            "input_description": r"输入描述:<br />　　第一行为一个整数n，表示集合A中的元素个数。<br /> 　　第二行有n个互不相同的用空格隔开的整数，表示集合A中的元素。<br /> 　　第三行为一个整数m，表示集合B中的元素个数。<br /> 　　第四行有m个互不相同的用空格隔开的整数，表示集合B中的元素。<br /> 　　集合中的所有元素均为int范围内的整数，n、m&lt;=1000。 <br />输入样例: <br />5<br /> 1 2 3 4 5<br /> 5<br /> 2 4 6 8 10",
            "output_description": r"<br />输出描述: <br />　　第一行按从小到大的顺序输出A、B交集中的所有元素。<br /> 　　第二行按从小到大的顺序输出A、B并集中的所有元素。<br /> 　　第三行按从小到大的顺序输出B在A中的余集中的所有元素。<br /> 输出样例: <br />2 4<br /> 1 2 3 4 5 6 8 10<br /> 1 3 5",

            "test_case_id": "531040084118",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.55Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 53 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T53",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1056,
        "fields": {
            "title": "算法训练 瓷砖铺放",
            "description": r"<br />　　有一长度为N(1&lt;=Ｎ&lt;=10)的地板，给定两种不同瓷砖：一种长度为1，另一种长度为2，数目不限。要将这个长度为N的地板铺满，一共有多少种不同的铺法？<br /> 　　例如，长度为4的地面一共有如下5种铺法：<br /> 　　4=1+1+1+1<br /> 　　4=2+1+1<br /> 　　4=1+2+1<br /> 　　4=1+1+2<br /> 　　4=2+2<br /> 　　编程用递归的方法求解上述问题。",
            "input_description": r"输入描述:<br />　　只有一个数N，代表地板的长度 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出一个数，代表所有不同的瓷砖铺放方法的总数<br /> 输出样例: <br />",

            "test_case_id": "551078605752",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.57Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 55 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T55",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1073,
        "fields": {
            "title": "算法训练 幂方分解",
            "description": r"<br />　　任何一个正整数都可以用2的幂次方表示。例如：<br /> 　　137=2<sup>7</sup>+2<sup>3</sup>+2<sup>0         </sup><br /> 　　同时约定方次用括号来表示，即a<sup>b</sup> 可表示为a（b）。<br /> 　　由此可知，137可表示为：<br /> 　　2（7）+2（3）+2（0）<br /> 　　进一步：7= 2<sup>2</sup>+2+2<sup>0   </sup>（2<sup>1</sup>用2表示）<br /> 　　3=2+2<sup>0   </sup><br /> 　　所以最后137可表示为：<br /> 　　2（2（2）+2+2（0））+2（2+2（0））+2（0）<br /> 　　又如：<br /> 　　1315=2<sup>10</sup> +2<sup>8</sup> +2<sup>5</sup> +2+1<br /> 　　所以1315最后可表示为：<br /> 　　2（2（2+2（0））+2）+2（2（2+2（0）））+2（2（2）+2（0））+2+2（0）",
            "input_description": r"输入描述:<br />　　输入包含一个正整数N（N&lt;=20000），为要求分解的整数。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　程序输出包含一行字符串，为符合约定的n的0，2表示（在表示中不能有空格）<br /> 输出样例: <br />",

            "test_case_id": "721406039641",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.74Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 72 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T72",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1074,
        "fields": {
            "title": "算法训练 拦截导弹",
            "description": r"<br />　　某国为了防御敌国的导弹袭击，发展出一种导弹拦截系统。但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于前一发的高度。某天，雷达捕捉到敌国的导弹来袭。由于该系统还在试用阶段，所以只有一套系统，因此有可能不能拦截所有的导弹。<br /> <br /> 　　输入导弹依次飞来的高度（雷达给出的高度数据是不大于30000的正整数），计算这套系统最多能拦截多少导弹，如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。",
            "input_description": r"输入描述:<br />　　一行，为导弹依次飞来的高度 <br />输入样例: <br />389 207 155 300 299 170 158 65",
            "output_description": r"<br />输出描述: <br />　　两行，分别是最多能拦截的导弹数与要拦截所有导弹最少要配备的系统数<br /> 输出样例: <br />6<br /> 2",

            "test_case_id": "731425300458",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.75Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 73 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T73",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1075,
        "fields": {
            "title": "算法训练 回文数",
            "description": r"<br />　　若一个数（首位不为零）从左向右读与从右向左读都一样，我们就将其称之为回文数。<br /> 　　例如：给定一个10进制数56，将56加65（即把56从右向左读），得到121是一个回文数。<br /> <br /> 　　又如：对于10进制数87：<br /> 　　STEP1：87+78  = 165                  STEP2：165+561 = 726<br /> 　　STEP3：726+627 = 1353                STEP4：1353+3531 = 4884<br /> <br /> 　　在这里的一步是指进行了一次N进制的加法，上例最少用了4步得到回文数4884。<br /> <br /> 　　写一个程序，给定一个N（2&lt;=N&lt;=10或N=16）进制数M（其中16进制数字为0-9与A-F），求最少经过几步可以得到回文数。<br /> 　　如果在30步以内（包含30步）不可能得到回文数，则输出“Impossible!”",
            "input_description": r"输入描述:<br />　　两行，N与M <br />输入样例: <br />9<br /> 87",
            "output_description": r"<br />输出描述: <br />　　如果能在30步以内得到回文数，输出“STEP=xx”（不含引号），其中xx是步数；否则输出一行”Impossible!”（不含引号）<br /> 输出样例: <br />STEP=6",

            "test_case_id": "741444561275",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.76Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 74 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T74",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1076,
        "fields": {
            "title": "算法训练 旅行家的预算",
            "description": r"<br />　　一个旅行家想驾驶汽车以最少的费用从一个城市到另一个城市（假设出发时油箱是空的）。给定两个城市之间的距离D1、汽车油箱的容量C（以升为单位）、每升汽油能行驶的距离D2、出发点每升汽油价格P和沿途油站数N（N可以为零），油站i离出发点的距离Di、每升汽油价格Pi（i=1，2，……N）。计算结果四舍五入至小数点后两位。如果无法到达目的地，则输出“No Solution”。",
            "input_description": r"输入描述:<br />　　第一行为4个实数D1、C、D2、P与一个非负整数N；<br /> 　　接下来N行，每行两个实数Di、Pi。 <br />输入样例: <br />275.6 11.9 27.4 2.8 2<br /> 102.0 2.9<br /> 220.0 2.2",
            "output_description": r"<br />输出描述: <br />　　如果可以到达目的地，输出一个实数（四舍五入至小数点后两位），表示最小费用；否则输出“No Solution”（不含引号）。<br /> 输出样例: <br />26.95",

            "test_case_id": "751463822092",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.77Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 75 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T75",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1077,
        "fields": {
            "title": "算法训练 进制转换",
            "description": r"<br /><b>问题描述</b><b>   </b><br /> <br /> 　　我们可以用这样的方式来表示一个十进制数： 将每个阿拉伯数字乘以一个以该数字所处位置的（值减１）为指数，以１０为底数的幂之和的形式。例如：１２３可表示为 １＊１０<sup>２</sup>＋２＊１０<sup>１</sup>＋３＊１０<sup>０</sup>这样的形式。<br /> 　　与之相似的，对二进制数来说，也可表示成每个二进制数码乘以一个以该数字所处位置的（值－１）为指数，以２为底数的幂之和的形式。一般说来，任何一个正整数Ｒ或一个负整数－Ｒ都可以被选来作为一个数制系统的基数。如果是以Ｒ或－Ｒ为基数，则需要用到的数码为 ０，１，．．．．Ｒ－１。例如，当Ｒ＝７时，所需用到的数码是０，１，２，３，４，５和６，这与其是Ｒ或－Ｒ无关。如果作为基数的数绝对值超过１０，则为了表示这些数码，通常使用英文字母来表示那些大于９的数码。例如对１６进制数来说，用Ａ表示１０，用Ｂ表示１１，用Ｃ表示１２，用Ｄ表示１３，用Ｅ表示１４，用Ｆ表示１５。<br /> 　　在负进制数中是用－Ｒ 作为基数，例如－１５（十进制）相当于１１０００１（－２进制），并且它可以被表示为２的幂级数的和数：<br /> 　　１１０００１＝１＊（－２）<sup>５</sup>＋１＊（－２）<sup>４</sup>＋０＊（－２）<sup>３</sup>＋０＊（－２）<sup>２</sup>＋<br /> 　　０＊（－２）<sup>１</sup> ＋１＊（－２）<sup>０</sup><br /> 　　<sup>  </sup>  设计一个程序，读入一个十进制数和一个负进制数的基数, 并将此十进制数转换为此负进制下的数：     －Ｒ∈｛－２，－３，－４，．．．，－２０｝<br /> <br /> <b>输</b><b>入格式</b><b>   </b><br /> 　　一行两个数，第一个是十进制数Ｎ（－32768＜＝Ｎ＜＝32767），  第二个是负进制数的基数－Ｒ。<br /> <br /> <b>输</b>出格式<b>   </b><br /> 　　输出所求负进制数及其基数，若此基数超过１０，则参照１６进制的方式处理。（格式参照样例）<br /> <br /> 　　<b>样</b><b>例</b>输入1<br /> 　　30000 -2",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />30000=11011010101110000(base-2)",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />-20000 -2",

            "test_case_id": "761483082909",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.78Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 76 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T76",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1078,
        "fields": {
            "title": "算法训练 乘积最大",
            "description": r"<br /><b>问题描述</b><b>   </b><br /> <br /> 　　今年是国际数学联盟确定的“2000——世界数学年”，又恰逢我国著名数学家华罗庚先生诞辰90周年。在华罗庚先生的家乡江苏金坛，组织了一场别开生面的数学智力竞赛的活动，你的一个好朋友XZ也有幸得以参加。活动中，主持人给所有参加活动的选手出了这样一道题目：<br /> <br /> 　　设有一个长度为N的数字串，要求选手使用K个乘号将它分成K+1个部分，找出一种分法，使得这K+1个部分的乘积能够为最大。<br /> <br /> 　　同时，为了帮助选手能够正确理解题意，主持人还举了如下的一个例子：<br /> <br /> 　　有一个数字串：312， 当N=3，K=1时会有以下两种分法：<br /> <br /> 　　3*12=36<br /> 　　31*2=62<br /> <br /> 　　这时，符合题目要求的结果是：31*2=62<br /> <br /> 　　现在，请你帮助你的好朋友XZ设计一个程序，求得正确的答案。<br /> <br /> <b>输</b><b>入格式</b><b>   </b><br /> <br /> 　　程序的输入共有两行：<br /> 　　第一行共有2个自然数N，K（6≤N≤40，1≤K≤6）<br /> 　　第二行是一个长度为N的数字串。<br /> <br /> <br /> <b>输</b><b>出格式</b><b>   </b><br /> <br /> 　　输出所求得的最大乘积（一个自然数）。<br /> <br /> 　　<b>样</b><b>例</b>输入<br /> <br /> 　　4  2<br /> 　　1231",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />62",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "771502343726",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.79Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 77 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T77",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1079,
        "fields": {
            "title": "算法训练 单词接龙",
            "description": r"<br /><b>问题描述</b><b>   </b><br /> <br /> 　　单词接龙是一个与我们经常玩的成语接龙相类似的游戏，现在我们已知一组单词，且给定一个开头的字母，要求出以这个字母开头的最长的“龙”（每个单词都最多在“龙”中出现两次），在两个单词相连时，其重合部分合为一部分，例如 beast和astonish，如果接成一条龙则变为beastonish，另外相邻的两部分不能存在包含关系，例如at 和 atide 间不能相连。<br /> <br /> <b>输</b><b>入格式</b><b>  </b><br /> <br /> 　　输入的第一行为一个单独的整数n (n&lt;=20)表示单词数，以下n 行每行有一个单词，输入的最后一行为一个单个字符，表示“龙”开头的字母。你可以假定以此字母开头的“龙”一定存在.<br /> <br /> <b>输</b><b>出格式</b><b>  </b><br /> <br /> 　　只需输出以此字母开头的最长的“龙”的长度<br /> <br /> <b>样</b><b>例输入</b><br /> 　　5<br /> 　　at<br /> 　　touch<br /> 　　cheat<br /> 　　choose<br /> 　　tact<br /> 　　a",
            "input_description": r"输入描述:<br />　　连成的“龙”为atoucheatactactouchoose <br />输入样例: <br />23",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "781521604543",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.80Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 78 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T78",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1080,
        "fields": {
            "title": "算法训练 方格取数",
            "description": r"<br /><b>问题描述</b><b>   </b><br /> 　　设有N*N的方格图(N&lt;=10),我们将其中的某些方格中填入正整数,而其他的方格中则放入数字0。<br /> 　　某人从图的左上角的A 点(1,1)出发，可以向下行走，也可以向右走，直到到达右下角的B点(N,N)。在走过的路上，他可以取走方格中的数（取走后的方格中将变为数字0）。<br /> 　　此人从A点到B 点共走两次，试找出2条这样的路径，使得取得的数之和为最大。<br /> <b>输</b><b>入格式</b><br /> 　　输入的第一行为一个整数N（表示N*N的方格图），接下来的每行有三个整数，前两个表示位置，第三个数为该位置上所放的数。一行单独的0表示输入结束。<br /> <b>输</b><b>出格式</b><br /> 　　只需输出一个整数，表示2条路径上取得的最大的和。<br /> <b>样</b><b>例</b><b>输</b><b>入</b><br /> 　　8<br /> 　　2 3 13<br /> 　　2 6 6<br /> 　　3 5 7<br /> 　　4 4 14<br /> 　　5 2 21<br /> 　　5 6 4<br /> 　　6 3 15<br /> 　　7 2 14<br /> 　　0 0 0<br /> <b>样例输出</b><br /> 　　67",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "791540865360",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.81Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 79 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T79",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1083,
        "fields": {
            "title": "算法训练 求先序排列",
            "description": r"<br /><b>问题描述</b><br /> 　　给出一棵二叉树的中序与后序排列。求出它的先序排列。（约定树结点用不同的大写字母表示，长度&lt;=8）。",
            "input_description": r"输入描述:<br />　　两行，每行一个字符串，分别表示中序和后序排列 <br />输入样例: <br />ABCD",
            "output_description": r"<br />输出描述: <br />　　一个字符串，表示所求先序排列<br /> <br /> 　　<b>样例</b>输入<br /> 　　BADC<br /> 　　BDCA<br /> 输出样例: <br />",

            "test_case_id": "821598647811",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.84Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 82 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T82",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1084,
        "fields": {
            "title": "算法训练 装箱问题",
            "description": r"<br /><b>问题描述</b><br /> 　　有一个箱子容量为V（正整数，0＜＝V＜＝20000），同时有n个物品（0＜n＜＝30），每个物品有一个体积（正整数）。<br /> 　　要求n个物品中，任取若干个装入箱内，使箱子的剩余空间为最小。",
            "input_description": r"输入描述:<br />　　第一行为一个整数，表示箱子容量；<br /> 　　第二行为一个整数，表示有n个物品；<br /> 　　接下来n行，每行一个整数表示这n个物品的各自体积。 <br />输入样例: <br />0",
            "output_description": r"<br />输出描述: <br />　　一个整数，表示箱子剩余空间。<br /> 　　<b>样例</b>输入<br /> 　　24<br /> 　　6<br /> 　　8<br /> 　　3<br /> 　　12<br /> 　　7<br /> 　　9<br /> 　　7<br /> 输出样例: <br />",

            "test_case_id": "831617908628",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.85Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 83 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T83",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1085,
        "fields": {
            "title": "算法训练 数的划分",
            "description": r"<br />　　将整数n分成k份，且每份不能为空，任意两份不能相同(不考虑顺序)。<br /> 　　例如：n=7，k=3，下面三种分法被认为是相同的。<br /> 　　1，1，5;        1，5，1; 5，1，1;<br /> 　　问有多少种不同的分法。",
            "input_description": r"输入描述:<br />　　n，k <br />输入样例: <br />7 3",
            "output_description": r"<br />输出描述: <br />　　一个整数，即不同的分法<br /> 输出样例: <br />4      {四种分法为：1，1，5;1，2，4;1，3，3;2，2，3;}",

            "test_case_id": "841637169445",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　6&lt;n&lt;=200，2&lt;=k&lt;=6",
            "create_time": "2018-02-28T03:15:44.86Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 84 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T84",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1086,
        "fields": {
            "title": "算法训练 一元三次方程求解",
            "description": r"<br />　　有形如：ax<sup>3</sup>+bx<sup>2</sup>+cx+d=0  这样的一个一元三次方程。给出该方程中各项的系数(a，b，c，d  均为实数)，并约定该方程存在三个不同实根(根的范围在-100至100之间)，且根与根之差的绝对值&gt;=1。要求三个实根。。",
            "input_description": r"输入描述:<br />　　四个实数：a，b，c，d <br />输入样例: <br />1   -5   -4   20",
            "output_description": r"<br />输出描述: <br />　　由小到大依次在同一行输出这三个实根(根与根之间留有空格)，并精确到小数点后2位<br /> 输出样例: <br />-2.00          2.00   5.00",

            "test_case_id": "851656430262",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　|a|，|b|，|c|，|d|&lt;=10",
            "create_time": "2018-02-28T03:15:44.87Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 85 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T85",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1087,
        "fields": {
            "title": "算法训练 统计单词个数",
            "description": r"<br />　　给出一个长度不超过200的由小写英文字母组成的字母串(约定;该字串以每行20个字母的方式输入，且保证每行一定为20个)。要求将此字母串分成k份 (1&lt;k&lt;=40)，且每份中包含的单词个数加起来总数最大(每份中包含的单词可以部分重叠。当选用一个单词之后，其第一个字母不能再用。例 如字符串this中可包含this和is，选用this之后就不能包含th)。<br /> 　　单词在给出的一个不超过6个单词的字典中。<br /> 　　要求输出最大的个数。",
            "input_description": r"输入描述:<br />　　第一行有二个正整数(p，k)<br /> 　　p表示字串的行数;<br /> 　　k表示分为k个部分。<br /> 　　接下来的p行，每行均有20个字符。<br /> 　　再接下来有一个正整数s，表示字典中单词个数。(1&lt;=s&lt;=6)<br /> 　　接下来的s行，每行均有一个单词。 <br />输入样例: <br />1        3<br /> thisisabookyouareaoh<br /> 4<br /> is<br /> a<br /> ok<br /> sab",
            "output_description": r"<br />输出描述: <br />　　每行一个整数，分别对应每组测试数据的相应结果。<br /> 输出样例: <br />7",

            "test_case_id": "861675691079",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　长度不超过200，1&lt;k&lt;=40，字典中的单词数不超过6。",
            "create_time": "2018-02-28T03:15:44.88Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 86 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T86",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1088,
        "fields": {
            "title": "算法训练 Car的旅行路线",
            "description": r"<br />　　又到暑假了，住在城市A的Car想和朋友一起去城市B旅游。她知道每个城市都有四个飞机场，分别位于一个矩形的四个顶点上，同一个城市中两个机场之间有一 条笔直的高速铁路，第I个城市中高速铁路了的单位里程价格为Ti，任意两个不同城市的机场之间均有航线，所有航线单位里程的价格均为t。<br /> 　　那么Car应如何安排到城市B的路线才能尽可能的节省花费呢?她发现这并不是一个简单的问题，于是她来向你请教。<br /> 　　找出一条从城市A到B的旅游路线，出发和到达城市中的机场可以任意选取，要求总的花费最少。",
            "input_description": r"输入描述:<br />　　的第一行有四个正整数s，t，A，B。<br /> 　　S表示城市的个数，t表示飞机单位里程的价格，A，B分别为城市A，B的序号，(1&lt;=A，B&lt;=S)。<br /> 　　接下来有S行，其中第I行均有7个正整数xi1，yi1，xi2，yi2，xi3，yi3，Ti，这当中的(xi1，yi1)，(xi2，yi2)，(xi3，yi3)分别是第I个城市中任意三个机场的坐标，T        I为第I个城市高速铁路单位里程的价格。 <br />输入样例: <br />1<br /> 1 10 1 3<br /> 1 1 1 3 3 1 30<br /> 2 5 7 4 5 2        1<br /> 8 6 8 8 11 6 3",
            "output_description": r"<br />输出描述: <br />　　共有n行，每行一个数据对应测试数据，保留一位小数。<br /> 输出样例: <br />47.55",

            "test_case_id": "871694951896",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　0&lt;S&lt;=100，",
            "create_time": "2018-02-28T03:15:44.89Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 87 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T87",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1089,
        "fields": {
            "title": "算法训练 麦森数",
            "description": r"<br />　　形如2<i><sup>P</sup></i>-1的素数称为麦森数，这时P一定也是个素数。但反过来不一定，即如果P是个素数，2<i><sup>P</sup></i>-1不一定也是素数。到1998年底，人们已找到了37个麦森数。最大的一个是P=3021377，它有909526位。麦森数有许多重要应用，它与完全数密切相关。<br /> 　　任务：从文件中输入P（1000&lt;P&lt;3100000），计算2<i><sup>P</sup></i>-1的位数和最后500位数字（用十进制高精度数表示）",
            "input_description": r"输入描述:<br />　　文件中只包含一个整数P（1000&lt;P&lt;3100000） <br />输入样例: <br />1279",
            "output_description": r"<br />输出描述: <br />　　第一行：十进制高精度数2<i><sup>P</sup></i>-1的位数。<br /> 　　第2-11行：十进制高精度数2<i><sup>P</sup></i>-1的最后500位数字。（每行输出50位，共输出10行，不足500位时高位补0）<br /> 　　不必验证2<i><sup>P</sup></i>-1与P是否为素数。<br /> 输出样例: <br />386<br /> 00000000000000000000000000000000000000000000000000<br /> 00000000000000000000000000000000000000000000000000<br /> 00000000000000104079321946643990819252403273640855<br /> 38615262247266704805319112350403608059673360298012<br /> 23944173232418484242161395428100779138356624832346<br /> 49081399066056773207629241295093892203457731833496<br /> 61583550472959420547689811211693677147548478866962<br /> 50138443826029173234888531116082853841658502825560<br /> 46662248318909188018470682222031405210266984354887<br /> 32958028878050869736186900714720710555703168729087",

            "test_case_id": "881714212713",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.90Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 88 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T88",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1090,
        "fields": {
            "title": "算法训练 FBI树",
            "description": r"<br />　　我们可以把由“0”和“1”组成的字符串分为三类：全“0”串称为B串，全“1”串称为I串，既含“0”又含“1”的串则称为F串。<br /> 　　FBI树是一种二叉树，它的结点类型也包括F结点，B结点和I结点三种。由一个长度为2<sup>N</sup>的“01”串S可以构造出一棵FBI树T，递归的构造方法如下：<br /> 　　1)T的根结点为R，其类型与串S的类型相同；<br /> 　　2)若串S的长度大于1，将串S从中间分开，分为等长的左右子串S1和S2；由左子串S1构造R的左子树T1，由右子串S2构造R的右子树T2。<br /> 　　现在给定一个长度为2<sup>N</sup>的“01”串，请用上述构造方法构造出一棵FBI树，并输出它的后序遍历序列。",
            "input_description": r"输入描述:<br />　　第一行是一个整数N（0  &lt;= N &lt;= 10），第二行是一个长度为2<sup>N</sup>的“01”串。 <br />输入样例: <br />3<br /> 10001011",
            "output_description": r"<br />输出描述: <br />　　包括一行，这一行只包含一个字符串，即FBI树的后序遍历序列。<br /> 输出样例: <br />IBFBBBFIBFIIIFF",

            "test_case_id": "891733473530",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于40%的数据，N  &lt;= 2；<br /> 　　对于全部的数据，N  &lt;= 10。<br /> 　　注：<br /> 　　[1]   二叉树：二叉树是结点的有限集合，这个集合或为空集，或由一个根结点和两棵不相交的二叉树组成。这两棵不相交的二叉树分别称为这个根结点的左子树和右子树。<br /> 　　[2]   后序遍历：后序遍历是深度优先遍历二叉树的一种方法，它的递归定义是：先后序遍历左子树，再后序遍历右子树，最后访问根。",
            "create_time": "2018-02-28T03:15:44.91Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 89 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T89",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1091,
        "fields": {
            "title": "算法训练 星际交流",
            "description": r"<br />　　人类终于登上了火星的土地并且见到了神秘的火星人。人类和火星人都无法理解对方的语言，但是我们的科学家发明了一种用数字交流的方法。这种交流方法是这样 的，首先，火星人把一个非常大的数字告诉人类科学家，科学家破解这个数字的含义后，再把一个很小的数字加到这个大数上面，把结果告诉火星人，作为人类的回 答。<br /> 　　火星人用一种非常简单的方式来表示数字——掰手指。火星人只有一只手，但这只手上有成千上万的手指，这些手指排成一列，分别编号为1，2，3……。火星人的任意两根手指都能随意交换位置，他们就是通过这方法计数的。<br /> 　　一个火星人用一个人类的手演示了如何用手指计数。如果把五根手指——拇指、食指、中指、无名指和小指分别编号为1，2，3，4和5，当它们按正常顺序排列 时，形成了5位数12345，当你交换无名指和小指的位置时，会形成5位数12354，当你把五个手指的顺序完全颠倒时，会形成54321，在所有能够形 成的120个5位数中，12345最小，它表示1；12354第二小，它表示2；54321最大，它表示120。下表展示了只有3根手指时能够形成的6个 3位数和它们代表的数字：<br /> 　　三进制数<br /> 　　123<br /> 　　132<br /> 　　213<br /> 　　231<br /> 　　312<br /> 　　321<br /> 　　代表的数字<br /> 　　1<br /> 　　2<br /> 　　3<br /> 　　4<br /> 　　5<br /> 　　6<br /> 　　现在你有幸成为了第一个和火星人交流的地球人。一个火星人会让你看他的手指，科学家会告诉你要加上去的很小的数。你的任务是，把火星人用手指表示的数与科 学家告诉你的数相加，并根据相加的结果改变火星人手指的排列顺序。输入数据保证这个结果不会超出火星人手指能表示的范围。",
            "input_description": r"输入描述:<br />　　包括三行，第一行有一个正整数N，表示火星人手指的数目（1 &lt;= N &lt;=  10000）。第二行是一个正整数M，表示要加上去的小整数（1 &lt;= M &lt;=  100）。下一行是1到N这N个整数的一个排列，用空格隔开，表示火星人手指的排列顺序。 <br />输入样例: <br />5<br /> 3<br /> 1 2 3 4 5",
            "output_description": r"<br />输出描述: <br />　　只有一行，这一行含有N个整数，表示改变后的火星人手指的排列顺序。每两个相邻的数中间用一个空格分开，不能有多余的空格。<br /> 输出样例: <br />1 2 4 5 3",

            "test_case_id": "901752734347",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于30%的数据，N&lt;=15；<br /> 　　对于60%的数据，N&lt;=50；<br /> 　　对于全部的数据，N&lt;=10000；",
            "create_time": "2018-02-28T03:15:44.92Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 90 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T90",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1092,
        "fields": {
            "title": "算法训练 校门外的树",
            "description": r"<br />　　某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；数 轴上的每个整数点，即0，1，2，……，L，都种有一棵树。<br /> 　　由于马路上有一些区域要用来建地铁。这些区域用它们在数轴上的起始点和终止点表示。已 知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树 都移走后，马路上还有多少棵树。",
            "input_description": r"输入描述:<br />　　输入文件的第一行有两个整数L（1 &lt;= L &lt;= 10000）和 M（1 &lt;= M &lt;=  100），L代表马路的长度，M代表区域的数目，L和M之间用一个空格隔开。接下来的M行每行包含两个不同的整数，用一个空格隔开，表示一个区域的起始点 和终止点的坐标。 <br />输入样例: <br />500 3<br /> 150 300<br /> 100 200<br /> 470 471",
            "output_description": r"<br />输出描述: <br />　　输出文件包括一行，这一行只包含一个整数，表示马路上剩余的树的数目。<br /> 输出样例: <br />298",

            "test_case_id": "911771995164",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于20%的数据，区域之间没有重合的部分；<br /> 　　对于其它的数据，区域之间有重合的情况。",
            "create_time": "2018-02-28T03:15:44.93Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 91 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T91",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1093,
        "fields": {
            "title": "算法训练 入学考试",
            "description": r"<br />　　辰辰是个天资聪颖的孩子，他的梦想是成为世界上最伟大的医师。为此，他想拜附近最有威望的医师为师。医师为了判断他的资质，给他出了一个难题。医师把他带到一个到处都是草药的山洞里对他说：“孩子，这个山洞里有一些不同的草药，采每一株都需要一些时间，每一株也有它自身的价值。我会给你一段时间，在这段时间里，你可以采到一些草药。如果你是一个聪明的孩子，你应该可以让采到的草药的总价值最大。”<br /> 　　如果你是辰辰，你能完成这个任务吗？",
            "input_description": r"输入描述:<br />　　第一行有两个整数T（1  &lt;= T &lt;= 1000）和M（1  &lt;= M &lt;= 100），用一个空格隔开，T代表总共能够用来采药的时间，M代表山洞里的草药的数目。接下来的M行每行包括两个在1到100之间（包括1和100）的整数，分别表示采摘某株草药的时间和这株草药的价值。 <br />输入样例: <br />70 3<br /> 71 100<br /> 69 1<br /> 1 2",
            "output_description": r"<br />输出描述: <br />　　包括一行，这一行只包含一个整数，表示在规定的时间内，可以采到的草药的最大总价值。<br /> 输出样例: <br />3",

            "test_case_id": "921791255981",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于30%的数据，M  &lt;= 10；<br /> 　　对于全部的数据，M  &lt;= 100。",
            "create_time": "2018-02-28T03:15:44.94Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 92 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T92",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1094,
        "fields": {
            "title": "算法训练 开心的金明",
            "description": r"<br />　　金明今天很开心，家里购置的新房就要领钥匙了，新房里有一间他自己专用的很宽敞的房间。更让他高兴的是，妈妈昨天对他说：“你的房间需要购买哪些物品，怎 么布置，你说了算，只要不超过N元钱就行”。今天一早金明就开始做预算，但是他想买的东西太多了，肯定会超过妈妈限定的N元。于是，他把每件物品规定了一 个重要度，分为5等：用整数1~5表示，第5等最重要。他还从因特网上查到了每件物品的价格（都是整数元）。他希望在不超过N元（可以等于N元）的前提 下，使每件物品的价格与重要度的乘积的总和最大。<br /> 　　设第j件物品的价格为v[j]，重要度为w[j]，共选中了k件物品，编号依次为 j1，j2，……，jk，则所求的总和为：<br /> 　　v[j1]*w[j1]+v[j2]*w[j2]+ …+v[jk]*w[jk]。（其中*为乘号）<br /> 　　请 你帮助金明设计一个满足要求的购物单。",
            "input_description": r"输入描述:<br />　　输入文件 的第1行，为两个正整数，用一个空格隔开：<br /> 　　N m<br /> 　　（其中N（&lt;30000）表示总钱 数，m（&lt;25）为希望购买物品的个数。）<br /> 　　从第2行到第m+1行，第j行给出了编号为j-1的物品的基本数据，每行有2个非负整数<br /> 　　v  p<br /> 　　（其中v表示该物品的价格(v&lt;=10000)，p表示该物品的重要度(1~5)） <br />输入样例: <br />1000 5<br /> 800 2<br /> 400 5<br /> 300 5<br /> 400 3<br /> 200 2",
            "output_description": r"<br />输出描述: <br />　　输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（&lt;100000000）。<br /> 输出样例: <br />3900",

            "test_case_id": "931810516798",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.95Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 93 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T93",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1095,
        "fields": {
            "title": "算法训练 JAM计数法",
            "description": r"<br />　　Jam是个喜欢标新立异的科学怪人。他不使用阿拉伯数字计数，而是使用<b>小写英文字母</b>计数，他觉得这样做，会使世界更加丰富多彩。在他的计数法中，每个数字的位数都是相同的（使用相同个数的字母），英文字母按原先的顺序，排在前面的字母小于排在它后面的字母。我们把这样的“数字”称为Jam数字。在Jam数字中，每个字母互不相同，而且<b>从左到右是严格递增</b>的。每次，Jam还指定使用字母的<b>范围</b>，例如，从2到10，表示只能使用{b,c,d,e,f,g,h,i,j}这些字母。如果再规定位数为5，那么，紧接在Jam数字“bdfij”之后的数字应该是“bdghi”。（如果我们用U、V依次表示Jam数字“bdfij”与“bdghi”，则U&lt;V&lt;  span&gt;，且不存在Jam数字P，使U&lt;P&lt;V&lt;  span&gt;）。你的任务是：对于从文件读入的一个Jam数字，按顺序输出紧接在后面的5个Jam数字，如果后面没有那么多Jam数字，那么有几个就输出几个。",
            "input_description": r"输入描述:<br />　　有2行，第1行为3个正整数，用一个空格隔开：<br /> 　　s t w<br /> 　　（其中s为所使用的最小的字母的序号，t为所使用的最大的字母的序号。w为数字的位数，这3个数满足：1≤s&lt;T≤26,  2≤w≤t-s ）<br /> 　　第2行为具有w个小写字母的字符串，为一个符合要求的Jam数字。<br /> 　　所给的数据都是正确的，不必验证。 <br />输入样例: <br />2 10 5<br /> bdfij",
            "output_description": r"<br />输出描述: <br />　　最多为5行，为紧接在输入的Jam数字后面的5个Jam数字，如果后面没有那么多Jam数字，那么有几个就输出几个。每行只输出一个Jam数字，是由w个小写字母组成的字符串，不要有多余的空格。<br /> 输出样例: <br />bdghi<br /> bdghj<br /> bdgij<br /> bdhij<br /> befgh",

            "test_case_id": "941829777615",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.96Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 94 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T94",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1096,
        "fields": {
            "title": "算法训练 数列",
            "description": r"<br />　　给定一个正整数k(3≤k≤15),把所有k的方幂及所有有限个互不相等的k的方幂之和构成一个递增的序列，例如，当k=3时，这个序列是：<br /> 　　1，3，4，9，10，12，13，…<br /> 　　（该序列实际上就是：3<sup>0</sup>，3<sup>1</sup>，3<sup>0</sup>+3<sup>1</sup>，3<sup>2</sup>，3<sup>0</sup>+3<sup>2</sup>，3<sup>1</sup>+3<sup>2</sup>，3<sup>0</sup>+3<sup>1</sup>+3<sup>2</sup>，…）<br /> 　　请你求出这个序列的第N项的值（用10进制数表示）。<br /> 　　例如，对于k=3，N=100，正确答案应该是981。",
            "input_description": r"输入描述:<br />　　只有1行，为2个正整数，用一个空格隔开：<br /> 　　k N<br /> 　　（k、N的含义与上述的问题描述一致，且3≤k≤15，10≤N≤1000）。 <br />输入样例: <br />3 100",
            "output_description": r"<br />输出描述: <br />　　计算结果，是一个正整数（在所有的测试数据中，结果均不超过2.1*10<sup>9</sup>）。（整数前不要有空格和其他符号）。<br /> 输出样例: <br />981",

            "test_case_id": "951849038432",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.97Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 95 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T95",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1097,
        "fields": {
            "title": "算法训练 纪念品分组",
            "description": r"<br />　　元旦快到了，校学生会让乐乐负责新年晚会的纪念品发放工作。为使得参加晚会的同学所获得的纪念品价值 相对均衡，他要把购来的纪念品根据价格进行分组，但每组最多只能包括两件纪念品，并且每组纪念品的价格之和不能超过一个给定的整数。为了保证在尽量短的时 间内发完所有纪念品，乐乐希望分组的数目最少。<br /> 　　你的任务是写一个程序，找出所有分组方案中分组数最少的一种，输出最少的分组数目。",
            "input_description": r"输入描述:<br />　　输入包含<i>n</i>+2行：<br /> 　　第1行包括一个整数<i>w</i>，为每组纪念品价格之和的上限。<br /> 　　第2行为一个整数<i>n</i>，表示购来的纪念品的总件数。<br /> 　　第3~<i>n</i>+2行每行包含一个正整数<i>p<sub>i</sub></i> (5  &lt;= <i>p<sub>i</sub></i> &lt;= <i>w</i>)，表示所对应纪念品的价格。 <br />输入样例: <br />100<br /> 9<br /> 90<br /> 20<br /> 20<br /> 30<br /> 50<br /> 60<br /> 70<br /> 80<br /> 90",
            "output_description": r"<br />输出描述: <br />　　输出仅一行，包含一个整数，即最少的分组数目。<br /> 输出样例: <br />6",

            "test_case_id": "961868299249",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　50%的数据满足：1 &lt;= <i>n</i> &lt;= 15<br /> 　　100%的数据满足：1 &lt;= <i>n</i> &lt;= 30000, 80 &lt;= <i>w</i> &lt;= 200",
            "create_time": "2018-02-28T03:15:44.98Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 96 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T96",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1098,
        "fields": {
            "title": "算法训练 传球游戏",
            "description": r"<br />　　<b>【</b>问题描述】<br /> 　　上体育课的时候，小蛮的老师经常带着同学们一起做游戏。这次，老师带着同学们一起做传球游戏。<br /> 　　游戏规则是这样的：n个同学站成一个圆圈，其中的一个同学手里拿着一个球，当老师吹哨子时开始传球，每个同学可以把球传给自己左右的两个同学中的一个（左右任意），当老师再次吹哨子时，传球停止，此时，拿着球没传出去的那个同学就是败者，要给大家表演一个节目。<br /> 　　聪明的小蛮提出一个有趣的问题：有多少种不同的传球方法可以使得从小蛮手里开始传的球，传了m次以后，又回到小蛮手里。两种传球的方法被视作不同的方法，当且仅当这两种方法中，接到球的同学按接球顺序组成的序列是不同的。比如有3个同学1号、2号、3号，并假设小蛮为1号，球传了3次回到小蛮手里的方式有1-&gt;2-&gt;3-&gt;1和1-&gt;3-&gt;2-&gt;1，共2种。",
            "input_description": r"输入描述:<br />　　共一行，有两个用空格隔开的整数n，m（3&lt;=n&lt;=30，1&lt;=m&lt;=30）。 <br />输入样例: <br />3 3",
            "output_description": r"<br />输出描述: <br />　　t共一行，有一个整数，表示符合题意的方法数。<br /> 输出样例: <br />2",

            "test_case_id": "971887560066",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　40%的数据满足：3&lt;=n&lt;=30，1&lt;=m&lt;=20<br /> 　　100%的数据满足：3&lt;=n&lt;=30，1&lt;=m&lt;=30",
            "create_time": "2018-02-28T03:15:44.99Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 97 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T97",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1099,
        "fields": {
            "title": "算法训练 传纸条",
            "description": r"<br />　　小渊和小轩是好朋友也是同班同学，他们在一起总有谈不完的话题。一次素质拓展活动中，班上同学安排做成一个m行n列的矩阵，而小渊和小轩被安排在矩阵对角线的两端，因此，他们就无法直接交谈了。幸运的是，他们可以通过传纸条来进行交流。纸条要经由许多同学传到对方手里，小渊坐在矩阵的左上角，坐标(1,1)，小轩坐在矩阵的右下角，坐标(m,n)。从小渊传到小轩的纸条只可以向下或者向右传递，从小轩传给小渊的纸条只可以向上或者向左传递。<br /> 　　在活动进行中，小渊希望给小轩传递一张纸条，同时希望小轩给他回复。班里每个同学都可以帮他们传递，但只会帮他们一次，也就是说如果此人在小渊递给小轩纸条的时候帮忙，那么在小轩递给小渊的时候就不会再帮忙。反之亦然。<br /> 　　还有一件事情需要注意，全班每个同学愿意帮忙的好感度有高有低（注意：小渊和小轩的好心程度没有定义，输入时用0表示），可以用一个0-100的自然数来表示，数越大表示越好心。小渊和小轩希望尽可能找好心程度高的同学来帮忙传纸条，即找到来回两条传递路径，使得这两条路径上同学的好心程度只和最大。现在，请你帮助小渊和小轩找到这样的两条路径。",
            "input_description": r"输入描述:<br />　　输入第一行有2个用空格隔开的整数m和n，表示班里有m行n列（1&lt;=m,n&lt;=50）。<br /> 　　接下来的m行是一个m*n的矩阵，矩阵中第i行j列的整数表示坐在第i行j列的学生的好心程度。每行的n个整数之间用空格隔开。 <br />输入样例: <br />3 3<br /> 0 3 9<br /> 2 8 5<br /> 5 7 0",
            "output_description": r"<br />输出描述: <br />　　输出一行，包含一个整数，表示来回两条路上参与传递纸条的学生的好心程度之和的最大值。<br /> 输出样例: <br />34",

            "test_case_id": "981906820883",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　30%的数据满足：1&lt;=<i>m</i>,<i>n</i>&lt;=10<br /> 　　100%的数据满足：1&lt;=<i>m</i>,<i>n</i>&lt;=50",
            "create_time": "2018-02-28T03:15:44.100Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 98 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T98",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1100,
        "fields": {
            "title": "算法训练 Hankson的趣味题",
            "description": r"<br />　　Hanks 博士是BT (Bio-Tech，生物技术) 领域的知名专家，他的儿子名叫Hankson。现 在，刚刚放学回家的Hankson 正在思考一个有趣的问题。 今天在课堂上，老师讲解了如何求两个正整数c1 和c2 的最大公约数和最小公倍数。现 在Hankson 认为自己已经熟练地掌握了这些知识，他开始思考一个“求公约数”和“求公 倍数”之类问题的“逆问题”，这个问题是这样的：已知正整数a0,a1,b0,b1，设某未知正整 数x 满足： 1． x 和a0 的最大公约数是a1； 2． x 和b0 的最小公倍数是b1。 Hankson 的“逆问题”就是求出满足条件的正整数x。但稍加思索之后，他发现这样的 x 并不唯一，甚至可能不存在。因此他转而开始考虑如何求解满足条件的x 的个数。请你帮 助他编程求解这个问题。",
            "input_description": r"输入描述:<br />　　输入第一行为一个正整数n，表示有n 组输入数据。<br /> <br /> 　　接下来的n 行每 行一组输入数据，为四个正整数a0，a1，b0，b1，每两个整数之间用一个空格隔开。输入 数据保证a0 能被a1 整除，b1 能被b0 整除。 <br />输入样例: <br />2<br /> 41 1 96 288<br /> 95 1 37 1776",
            "output_description": r"<br />输出描述: <br />　　输出共n 行。每组输入数据的输出结果占一行，为一个整数。<br /> 　　对于每组数据：若不存在这样的 x，请输出0； 若存在这样的 x，请输出满足条件的x 的个数；<br /> 输出样例: <br />6<br /> 2",

            "test_case_id": "991926081700",
            "hint": r"HINT:时间限制：1.0s  内存限制：64.0MB<br />　　第一组输入数据，x 可以是9、18、36、72、144、288，共有6 个。<br /> 　　第二组输入数据，x 可以是48、1776，共有2 个。",
            "create_time": "2018-02-28T03:15:44.101Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 99 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T99",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1101,
        "fields": {
            "title": "算法训练 接水问题",
            "description": r"<br />　　学校里有一个水房，水房里一共装有m 个龙头可供同学们打开水，每个龙头每秒钟的 供水量相等，均为1。 现在有n 名同学准备接水，他们的初始接水顺序已经确定。将这些同学按接水顺序从1 到n 编号，i 号同学的接水量为wi。接水开始时，1 到m 号同学各占一个水龙头，并同时打 开水龙头接水。当其中某名同学j 完成其接水量要求wj 后，下一名排队等候接水的同学k 马上接替j 同学的位置开始接水。这个换人的过程是瞬间完成的，且没有任何水的浪费。即 j 同学第x 秒结束时完成接水，则k 同学第x+1 秒立刻开始接水。若当前接水人数n’不足m， 则只有n’个龙头供水，其它m&minus;n’个龙头关闭。 现在给出n 名同学的接水量，按照上述接水规则，问所有同学都接完水需要多少秒。",
            "input_description": r"输入描述:<br />　　第1 行2 个整数n 和m，用一个空格隔开，分别表示接水人数和龙头个数。 第2 行n 个整数w1、w2、……、wn，每两个整数之间用一个空格隔开，wi 表示i 号同 学的接水量。 <br />输入样例: <br />5 3<br /> 4 4 1 2 1",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，1 个整数，表示接水所需的总时间。<br /> 输出样例: <br />4",

            "test_case_id": "1001945342517",
            "hint": r"HINT:时间限制：1.0s  内存限制：64.0MB<br />　　第1 秒，3 人接水。第1 秒结束时，1、2、3 号同学每人的已接水量为1，3 号同学接完<br /> 　　水，4 号同学接替3 号同学开始接水。<br /> 　　第2 秒，3 人接水。第2 秒结束时，1、2 号同学每人的已接水量为2，4 号同学的已接<br /> 　　水量为1。<br /> 　　第3 秒，3 人接水。第3 秒结束时，1、2 号同学每人的已接水量为3，4 号同学的已接<br /> 　　水量为2。4 号同学接完水，5 号同学接替4 号同学开始接水。<br /> 　　第4 秒，3 人接水。第4 秒结束时，1、2 号同学每人的已接水量为4，5 号同学的已接<br /> 　　水量为1。1、2、5 号同学接完水，即所有人完成接水。<br /> 　　总接水时间为4 秒。",
            "create_time": "2018-02-28T03:15:44.102Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 100 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T100",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1102,
        "fields": {
            "title": "算法训练 A+B Problem",
            "description": r"<br />　　输入A,B。<br /> 　　输出A+B。",
            "input_description": r"输入描述:<br />　　输入包含两个整数A,B，用一个空格分隔。 <br />输入样例: <br />5 8",
            "output_description": r"<br />输出描述: <br />　　输出一个整数，表示A+B的值。<br /> 输出样例: <br />13",

            "test_case_id": "1031964603334",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　-1,000,000,000&lt;=A,B&lt;=1,000,000,000。",
            "create_time": "2018-02-28T03:15:44.103Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 103 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T103",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1103,
        "fields": {
            "title": "算法训练 采油区域",
            "description": r"<br />　　采油区域　　Siruseri政府决定将石油资源丰富的Navalur省的土地拍卖给私人承包商以建立油井。被拍卖的整块土地为一个矩形区域，被划分为<i>M</i>×<i>N</i>个小块。<br /> 　　Siruseri地质调查局有关于Navalur土地石油储量的估测数据。这些数据表示为<i>M</i>×<i>N</i>个非负整数，即对每一小块土地石油储量的估计值。<br /> 　　为了避免出现垄断，政府规定每一个承包商只能承包一个由<i>K</i>×<i>K</i>块相连的土地构成的正方形区域。<br /> 　　AoE石油联合公司由三个承包商组成，他们想选择三块互不相交的<i>K</i>×<i>K</i>的区域使得总的收益最大。<br /> 　　例如，假设石油储量的估计值如下：<br /> <br /> <table cellspacing=0 cellpadding=2px style='border-collapse:collapse;' class='table table-striped table-horver'><tbody><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>8<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td></tr></tbody></table><br /> <br /> 　　如果<i>K</i> = 2, AoE公司可以承包的区域的石油储量总和为100, 如果<i>K</i> = 3, AoE公司可以承包的区域的石油储量总和为208。<br /> 　　AoE公司雇佣你来写一个程序，帮助计算出他们可以承包的区域的石油储量之和的最大值。",
            "input_description": r"输入描述:<br />　　输入第一行包含三个整数<i>M</i>, <i>N</i>, <i>K</i>，其中<i>M</i>和<i>N</i>是矩形区域的行数和列数，<i>K</i>是每一个承包商承包的正方形的大小（边长的块数）。接下来<i>M</i>行，每行有<i>N</i>个非负整数表示这一行每一小块土地的石油储量的估计值。 <br />输入样例: <br />9 9 3<br /> 1 1 1 1 1 1 1 1 1<br /> 1 1 1 1 1 1 1 1 1<br /> 1 8 8 8 8 8 1 1 1<br /> 1 8 8 8 8 8 1 1 1<br /> 1 8 8 8 8 8 1 1 1<br /> 1 1 1 1 8 8 8 1 1<br /> 1 1 1 1 1 1 8 8 8<br /> 1 1 1 1 1 1 9 9 9<br /> 1 1 1 1 1 1 9 9 9",
            "output_description": r"<br />输出描述: <br />　　输出只包含一个整数，表示AoE公司可以承包的区域的石油储量之和的最大值。<br /> 输出样例: <br />208",

            "test_case_id": "1041983864151",
            "hint": r"HINT:时间限制：2.0s  内存限制：512.0MB<br />　　数据保证<i>K</i>≤<i>M</i>且<i>K</i>≤<i>N</i>并且至少有三个<i>K</i>×<i>K</i>的互不相交的正方形区域。其中30%的输入数据，<i>M</i>, <i>N</i>≤ 12。所有的输入数据, <i>M</i>, <i>N</i>≤ 1500。每一小块土地的石油储量的估计值是非负整数且≤ 500。",
            "create_time": "2018-02-28T03:15:44.104Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 104 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T104",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1104,
        "fields": {
            "title": "算法训练 会议中心",
            "description": r"<br />　　会议中心　　Siruseri政府建造了一座新的会议中心。许多公司对租借会议中心的会堂很感兴趣，他们希望能够在里面举行会议。<br /> 　　对于一个客户而言，仅当在开会时能够独自占用整个会堂，他才会租借会堂。会议中心的销售主管认为：最好的策略应该是将会堂租借给尽可能多的客户。显然，有可能存在不止一种满足要求的策略。<br /> 　　例如下面的例子。总共有4个公司。他们对租借会堂发出了请求，并提出了他们所需占用会堂的起止日期（如下表所示）。<br /> <br /> <table cellspacing=0 cellpadding=2px style='border-collapse:collapse;' class='table table-striped table-horver'><tbody><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'><br /> </td><td valign=\"top\" style='border:solid 1.0pt'>开始日期<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>结束日期<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>公司1<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>4<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>公司2<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>9<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>11<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>公司3<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>13<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>19<br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>公司4<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>10<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>17<br /> </td></tr></tbody></table><br /> <br /> 　　上例中，最多将会堂租借给两家公司。租借策略分别是租给公司1和公司3，或是公司2和公司3，也可以是公司1和公司4。注意会议中心一天最多租借给一个公司，所以公司1和公司2不能同时租借会议中心，因为他们在第九天重合了。<br /> 　　销售主管为了公平起见，决定按照如下的程序来确定选择何种租借策略：首先，将租借给客户数量最多的策略作为候选，将所有的公司按照他们发出请求的顺序编号。对于候选策略，将策略中的每家公司的编号按升序排列。最后，选出其中字典序最小[1]的候选策略作为最终的策略。<br /> 　　例中，会堂最终将被租借给公司1和公司3：3个候选策略是{(1,3),(2,3),(1,4)}。而在字典序中(1,3)&lt;(1,4)&lt;(2,3)。<br /> 　　你的任务是帮助销售主管确定应该将会堂租借给哪些公司。<b></b>",
            "input_description": r"输入描述:<br />　　输入的第一行有一个整数<i>N</i>，表示发出租借会堂申请的公司的个数。第2到第<i>N</i>+1行每行有2个整数。第<i>i</i>+1行的整数表示第<i>i</i>家公司申请租借的起始和终止日期。对于每个公司的申请，起始日期为不小于1的整数，终止日期为不大于10<sup>9</sup>的整数。 <br />输入样例: <br />4<br /> 4 9<br /> 9 11<br /> 13 19<br /> 10 17",
            "output_description": r"<br />输出描述: <br />　　输出的第一行应有一个整数<i>M</i>，表示最多可以租借给多少家公司。第二行应列出<i>M</i>个数，表示最终将会堂租借给哪些公司。<br /> 输出样例: <br />2<br /> 1 3<br /> <br /> [1] 字典序指在字典中排列的顺序，如果序列<i>l</i><sub>1</sub>是序列<i>l</i><sub>2</sub>的前缀，或者对于<i>l</i><sub>1</sub>和<i>l</i><sub>2</sub>的第一个不同位置<i>j</i>，<i>l</i><sub>1</sub>[<i>j</i>]&lt;<i>l</i><sub>2</sub>[<i>j</i>]，则<i>l</i><sub>1</sub>比<i>l</i><sub>2</sub>小。",

            "test_case_id": "1052003124968",
            "hint": r"HINT:时间限制：2.0s  内存限制：512.0MB<br />　　对于50%的输入，<i>N</i>≤3000。在所有输入中，<i>N</i>≤200000。",
            "create_time": "2018-02-28T03:15:44.105Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 105 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T105",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1105,
        "fields": {
            "title": "算法训练 调和数列问题",
            "description": r"<br />　　输入一个实数x，求最小的n使得，1/2+1/3+1/4+...+1/(n+1)&gt;=x。<br /> <br /> 　　输入的实数x保证大于等于0.01，小于等于5.20，并且恰好有两位小数。你的程序要能够处理多组数据，即不停地读入x，如果x不等于0.00，则计算答案，否则退出程序。<br /> <br /> 　　输出格式为对于一个x，输出一行n card(s)。其中n表示要计算的答案。",
            "input_description": r"输入描述:<br />　　分行输入x的具体数值 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　分行输出n的数值，格式为n card(s)<br /> 输出样例: <br />",

            "test_case_id": "1072022385785",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.106Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 107 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T107",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1106,
        "fields": {
            "title": "算法训练 Hanoi问题",
            "description": r"<br />　　如果将课本上的Hanoi塔问题稍做修改：仍然是给定N只盘子，3根柱子，但是允许每次最多移动相邻的M只盘子（当然移动盘子的数目也可以小于M）,最少需要多少次？<br /> 　　例如N=5，M=2时，可以分别将最小的2个盘子、中间的2个盘子以及最大的一个盘子分别看作一个整体，这样可以转变为N=3，M=1的情况，共需要移动7次。",
            "input_description": r"输入描述:<br />　　输入数据仅有一行，包括两个数N和M（0&lt;=M&lt;=N&lt;=8） <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　仅输出一个数，表示需要移动的最少次数<br /> 输出样例: <br />",

            "test_case_id": "1082041646602",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.107Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 108 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T108",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1107,
        "fields": {
            "title": "算法训练 蜜蜂飞舞",
            "description": r"<br />　　“两只小蜜蜂呀，飞在花丛中呀……”<br /> <br /> 　　话说这天天上飞舞着两只蜜蜂，它们在跳一种奇怪的舞蹈。用一个空间直角坐标系来描述这个世界，那么这两只蜜蜂初始坐标分别为(x1,y1,z1)，(x2,y2,z2)　　。在接下来它们将进行n次飞行，第i次飞行两只蜜蜂分别按照各自的速度向量飞行ti个单位时间。对于这一现象，玮玮已经观察了很久。他很想知道在蜜蜂飞舞结束时，两只蜜蜂的距离是多少。现在他就求教于你，请你写一个程序来帮他计算这个结果。",
            "input_description": r"输入描述:<br />　　第一行有且仅有一个整数n，表示两只蜜蜂将进行n次飞行。<br /> <br /> 　　接下来有n行。<br /> <br /> 　　第i行有7个用空格分隔开的整数ai,bi,ci,di,ei,fi,ti　　，表示第一只蜜蜂单位时间的速度向量为(ai,bi,ci) ，第二只蜜蜂单位时间的速度向量为(di,ei,fi) ，它们飞行的时间为ti 。<br /> <br /> 　　最后一行有6个用空格分隔开的整数x1,y1,z1,x2,y2,z2，如题所示表示两只蜜蜂的初始坐标。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出仅包含一行，表示最后两只蜜蜂之间的距离。保留4位小数位。<br /> 输出样例: <br />",

            "test_case_id": "1092060907419",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.108Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 109 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T109",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1110,
        "fields": {
            "title": "算法训练 数组查找及替换",
            "description": r"<br />　　给定某整数数组和某一整数b。要求删除数组中可以被b整除的所有元素，同时将该数组各元素按从小到大排序。如果数组元素数值在A到Z的ASCII之间，替换为对应字母。元素个数不超过100，b在1至100之间。",
            "input_description": r"输入描述:<br />　　第一行为数组元素个数和整数b<br /> 　　第二行为数组各个元素 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　按照要求输出<br /> 输出样例: <br />",

            "test_case_id": "1282118689870",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.111Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 128 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T128",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1112,
        "fields": {
            "title": "算法训练 排列问题",
            "description": r"<br />　　求一个0～N-1的排列（即每个数只能出现一次），给出限制条件（一张N*N的表，第i行第j列的1或0，表示为j-1这个数不能出现在i-1这个数后面，并保证第i行第i列为0），将这个排列看成一个自然数，求从小到大排序第K个排列。",
            "input_description": r"输入描述:<br />　　N&lt;=10，K&lt;=500000 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　第一行为N和K,接下来的N行，每行N个数，0表示不能，1表示能<br /> 输出样例: <br />",

            "test_case_id": "1312157211504",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　所求的排列",
            "create_time": "2018-02-28T03:15:44.113Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 131 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T131",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1117,
        "fields": {
            "title": "算法训练 简单加法(基本型)",
            "description": r"<br />　　首先给出简单加法算式的定义：<br /> 　　如果有一个算式(i)+(i+1)+(i+2),(i&gt;=0)，在计算的过程中，没有任何一个数位出现了进位，则称其为简单的加法算式。<br /> 　　例如：i=3时，3+4+5=12，有一个进位，因此3+4+5不是一个简单的加法算式；又如i=112时，112+113+114=339，没有在任意数位上产生进位，故112+113+114是一个简单的加法算式。<br /> <br /> 　　问题：给定一个正整数n，问当i大于等于0且小于n时,有多少个算式(i)+(i+1)+(i+2)是简单加法算式。其中n&lt;10000。",
            "input_description": r"输入描述:<br />　　一个整数，表示n <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　一个整数,表示简单加法算式的个数<br /> 输出样例: <br />",

            "test_case_id": "1382253515589",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.118Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 138 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T138",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1118,
        "fields": {
            "title": "算法训练 矩阵加法",
            "description": r"<br />　　给定两个N×M的矩阵，计算其和。其中：<br /> 　　N和M大于等于1且小于等于100，矩阵元素的绝对值不超过1000。",
            "input_description": r"输入描述:<br />　　输入数据的第一行包含两个整数N、M，表示需要相加的两个矩阵的行数和列数。接下来2*N行每行包含M个数，其中前N行表示第一个矩阵，后N行表示第二个矩阵。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　你的程序需要输出一个N*M的矩阵，表示两个矩阵相加的结果。注意，输出中每行的最后不应有多余的空格，否则你的程序有可能被系统认为是Presentation　　Error<br /> 输出样例: <br />",

            "test_case_id": "1392272776406",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.119Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 139 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T139",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1120,
        "fields": {
            "title": "算法训练 邮票",
            "description": r"<br />　　给定一个信封，有N（1≤N≤100）个位置可以贴邮票，每个位置只能贴一张邮票。我们现在有M(M&lt;=100)种不同邮资的邮票，面值为X1,X2….Xm分（Xi是整数，1≤Xi≤255），每种都有N张。<br /> <br /> 　　显然，信封上能贴的邮资最小值是min(X1, X2, …, Xm)，最大值是 N*max(X1, X2, …,　　Xm)。由所有贴法得到的邮资值可形成一个集合（集合中没有重复数值），要求求出这个集合中是否存在从1到某个值的连续邮资序列，输出这个序列的最大值。<br /> <br /> 　　例如，N=4，M=2，面值分别为4分，1分，于是形成1，2，3，4，5，6，7，8，9，10，12，13，16的序列，而从1开始的连续邮资序列为1，2，3，4，5，6，7，8，9，10，所以连续邮资序列的最大值为10分。",
            "input_description": r"输入描述:<br />　　第一行：最多允许粘贴的邮票张数N；第二行：邮票种数M；第三行：空格隔开的M个数字，表示邮票的面值Xi。注意：Xi序列不一定是大小有序的！ <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　从1开始的连续邮资序列的最大值MAX。若不存在从1分开始的序列（即输入的邮票中没有1分面额的邮票），则输出0.<br /> 输出样例: <br />",

            "test_case_id": "1412311298040",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.121Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 141 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T141",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1123,
        "fields": {
            "title": "算法训练 删除多余括号",
            "description": r"<br />　　从键盘输入一个含有括号的四则运算表达式，要求去掉可能含有的多余的括号，结果要保持原表达式中变量和运算符的相对位置不变，且与原表达式等价,不要求化简。另外不考虑'+'　　'-'用作正负号的情况，即输入表达式不会出现(+a)或(-a)的情形。",
            "input_description": r"输入描述:<br />　　表达式字符串，长度不超过255,　　并且不含空格字符。表达式中的所有变量都是单个小写的英文字母, 运算符只有加+减-乘*除/等运算符号。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　去掉多余括号后的表达式<br /> 输出样例: <br />",

            "test_case_id": "1442369080491",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.124Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 144 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T144",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1125,
        "fields": {
            "title": "算法训练 矩阵乘方",
            "description": r"<br />　　给定一个矩阵A,一个非负整数b和一个正整数m，求A的b次方除m的余数。<br /> 　　其中一个nxn的矩阵除m的余数得到的仍是一个nxn的矩阵，这个矩阵的每一个元素是原矩阵对应位置上的数除m的余数。<br /> 　　要计算这个问题，可以将A连乘b次，每次都对m求余，但这种方法特别慢，当b较大时无法使用。下面给出一种较快的算法(用A^b表示A的b次方)：<br /> 　　若b=0，则A^b%m=I%m。其中I表示单位矩阵。<br /> 　　若b为偶数，则A^b%m=(A^(b/2)%m)^2%m，即先把A乘b/2次方对m求余，然后再平方后对m求余。<br /> 　　若b为奇数，则A^b%m=(A^(b-1)%m)*a%m，即先求A乘b-1次方对m求余，然后再乘A后对m求余。<br /> 　　这种方法速度较快，请使用这种方法计算A^b%m，其中A是一个2x2的矩阵，m不大于10000。",
            "input_description": r"输入描述:<br />　　输入第一行包含两个整数b, m，第二行和第三行每行两个整数，为矩阵A。 <br />输入样例: <br />2 2<br /> 1 1<br /> 0 1",
            "output_description": r"<br />输出描述: <br />　　输出两行，每行两个整数，表示A^b%m的值。<br /> 输出样例: <br />1 0<br /> 0 1",

            "test_case_id": "1482407602125",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.126Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 148 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T148",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1132,
        "fields": {
            "title": "算法训练 比赛安排",
            "description": r"<br />　　设有有2 <sup>n</sup>（n&lt;=6）个球队进行单循环比赛，计划在2 <sup>n</sup> – 1天内完成，每个队每天进行一场比赛。设计一个比赛的安排，使在2 <sup>n</sup> – 1天内每个队都与不同的对手比赛。",
            "input_description": r"输入描述:<br />　　输入文件matchplan.in共一行，输入n的数值。 <br />输入样例: <br />2",
            "output_description": r"<br />输出描述: <br />　　输出文件matchplan.out共（2 n – 1）行，第i行输出第i天的比赛安排。<br /> 　　格式为：&lt;i&gt; A-B，C-D，……。其中i是天数，A，B分别为比赛双方的编号，每行共2 <sup>n-1</sup>个比赛场次。<br /> 输出样例: <br />&lt;1&gt;1-2,3-4<br /> &lt;2&gt;1-3,2-4<br /> &lt;3&gt;1-4,2-3",

            "test_case_id": "1592542427844",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.133Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 159 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T159",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1133,
        "fields": {
            "title": "算法训练 字符串编辑",
            "description": r"<br />　　从键盘输入一个字符串（长度&lt;=40个字符），并以字符 ’.’ 结束。编辑功能有：<br /> 　　1    D：删除一个字符，命令的方式为： D  a  其中a为被删除的字符，例如：D  s  表示删除字符 ’s’ ，若字符串中有多个 ‘s’，则删除第一次出现的。<br /> 　　2    I：插入一个字符，命令的格式为：I  a1  a2  其中a1表示插入到指定字符前面，a2表示将要插入的字符。例如：I  s  d  表示在指定字符 ’s’ 的前面插入字符 ‘d’ ，若原串中有多个 ‘s’ ，则插入在最后一个字符的前面。<br /> 　　3   R：替换一个字符，命令格式为：R  a1  a2  其中a1为被替换的字符，a2为替换的字符，若在原串中有多个a1则应全部替换。<br /> 　　在编辑过程中，若出现被改的字符不存在时，则给出提示信息。",
            "input_description": r"输入描述:<br />　　输入共两行，第一行为原串(以’.’结束)，第二行为命令（输入方式参见“问题描述” 。 <br />输入样例: <br />This is a book.<br /> D s",
            "output_description": r"<br />输出描述: <br />　　输出共一行，为修改后的字符串或输出指定字符不存在的提示信息。<br /> 输出样例: <br />Thi is a book.",

            "test_case_id": "1602561688661",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　命令为删去s，第一个在字符中出现的s在This中，即得到结果。",
            "create_time": "2018-02-28T03:15:44.134Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 160 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T160",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1138,
        "fields": {
            "title": "算法训练 最长字符串",
            "description": r"<br />　　求出5个字符串中最长的字符串。每个字符串长度在100以内，且全为小写字母。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />one two three four five",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />three",

            "test_case_id": "1692657992746",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.139Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 169 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T169",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1139,
        "fields": {
            "title": "算法训练 比较字符串",
            "description": r"<br />　　编程实现两个字符串s1和s2的字典序比较。（保证每一个字符串不是另一个的前缀，且长度在100以内）。若s1和s2相等，输出0；若它们不相等，则指出其第一个不同字符的ASCII码的差值：如果s1&gt;s2，则差值为正；如果s1&lt;s2，则差值为负。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />java basic",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />8",

            "test_case_id": "1702677253563",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.140Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 170 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T170",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1144,
        "fields": {
            "title": "算法训练 筛选号码",
            "description": r"<br />　　有n个人围成一圈，顺序排号（编号为1到n）。从第1个人开始报数(从1到3报数)，凡报到3的人退出圈子。从下一个人开始继续报数，直到剩下最后一个人，游戏结束。<br /> 　　问最后留下的是原来第几号的那位。<br /> 　　举个例子，8个人围成一圈：<br /> 　　1 2 3 4 5 6 7 8<br /> 　　第1次报数之后，3退出，剩下：<br /> 　　1 2 4 5 6 7 8\t（现在从4开始报数）<br /> 　　第2次报数之后，6退出，剩下：<br /> 　　1 2 4 5 7 8\t\t（现在从7开始报数）<br /> 　　第3次报数之后，1退出，剩下：<br /> 　　2 4 5 7 8\t\t（现在从2开始报数）<br /> 　　第4次报数之后，5退出，剩下：<br /> 　　2 4 7 8\t\t\t（现在从7开始报数）<br /> 　　第5次报数之后，2退出，剩下：<br /> 　　4 7 8\t\t\t（现在从4开始报数）<br /> 　　第6次报数之后，8退出，剩下：<br /> 　　4 7\t\t\t\t（现在从4开始报数）<br /> 　　最后一次报数之后，4退出，剩下：<br /> 　　7.<br /> 　　所以，最后留下来的人编号是7。",
            "input_description": r"输入描述:<br />　　一个正整数n，(1&lt;n&lt;10000) <br />输入样例: <br />8",
            "output_description": r"<br />输出描述: <br />　　一个正整数，最后留下来的那个人的编号。<br /> 输出样例: <br />7",

            "test_case_id": "1822773557648",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　对于100%的数据，1&lt;n&lt;10000。",
            "create_time": "2018-02-28T03:15:44.145Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 182 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T182",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1146,
        "fields": {
            "title": "算法训练 斜率计算",
            "description": r"<br />　　输入两个点的坐标，即p1 = (x1, y1)和p2=(x2, y2)，求过这两个点的直线的斜率。如果斜率为无穷大输出“INF”。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1 2<br /> 2 4",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />2",

            "test_case_id": "1882812079282",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.147Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 188 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T188",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1152,
        "fields": {
            "title": "算法训练 确定元音字母位置",
            "description": r"<br />",
            "input_description": r"输入描述:<br /> <br />输入样例: <br /><pre class='pddata'> 输入一个字符串，编写程序输出该字符串中元音字母的首次出现位置，如果没有元音字母输出0。英语元音字母只有‘a’、‘e’、‘i’、‘o’、‘u’五个。 </pre>",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2002927644184",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.153Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 200 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T200",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1153,
        "fields": {
            "title": "算法训练 整数平均值",
            "description": r"<br />",
            "input_description": r"输入描述:<br /> <br />输入样例: <br /><pre class='pddata'> 编写函数，求包含n个元素的整数数组中元素的平均值。要求在函数内部使用指针操纵数组元素，其中n个整数从键盘输入，输出为其平均值。 </pre>",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2022946905001",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.154Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 202 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T202",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1156,
        "fields": {
            "title": "算法训练 输出米字形",
            "description": r"<br />　　根据输入的正整数n (1　　米字形由一个(2n-1)*(2n-1)的矩阵组成，矩阵包含从大写A开始的n个字母<br /> 　　例如:n=3时，包含A,B,C；n=4时，包含A,B,C,D。<br /> 　　矩阵的正中间为n个字母中字典序最大的那个，从这个字母开始，沿着西北、正北、东北、正西、正东、西南、正南、东南八个方向各有一条由大写字母组成的直线。并且直线上的字母按字典序依次减小，直到大写字母A。<br /> 　　矩阵的其它位置用英文句号．填充。<br /> <br /> 　　样例输入一<br /> 　　3<br /> <br /> 　　样例输出一<br /> 　　Ａ．Ａ．Ａ<br /> 　　．ＢＢＢ．<br /> 　　ＡＢＣＢＡ<br /> 　　．ＢＢＢ．<br /> 　　Ａ．Ａ．Ａ<br /> <br /> 　　样例输入二<br /> 　　4<br /> <br /> 　　样例输出二<br /> 　　Ａ．．Ａ．．Ａ<br /> 　　．Ｂ．Ｂ．Ｂ．<br /> 　　．．ＣＣＣ．．<br /> 　　ＡＢＣＤＣＢＡ<br /> 　　．．ＣＣＣ．．<br /> 　　．Ｂ．Ｂ．Ｂ．<br /> 　　Ａ．．Ａ．．Ａ",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2083004687452",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.157Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 208 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T208",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1159,
        "fields": {
            "title": "算法训练 阶乘",
            "description": r"<br /><b>问题描述</b><br /> 　　一个整数n的阶乘可以写成n!，它表示从1到n这n个整数的乘积。阶乘的增长速度非常快，例如，13!就已经比较大了，已经无法存放在一个整型变量中；而35!就更大了，它已经无法存放在一个浮点型变量中。因此，当n比较大时，去计算n!是非常困难的。幸运的是，在本题中，我们的任务不是去计算n!，而是去计算n!最右边的那个非0的数字是多少。例如，5! = 1*2*3*4*5 = 120，因此5!最右边的那个非0的数字是2。再如：7! = 5040，因此7!最右边的那个非0的数字是4。请编写一个程序，输入一个整数n(n&lt;=100)，然后输出n! 最右边的那个非0的数字是多少。<br /> 　　输入格式：输入只有一个整数n。<br /> 　　输出格式：输出只有一个整数，即n! 最右边的那个非0的数字。<br /> <b>输入输出样例</b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />6",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />2",

            "test_case_id": "2133062469903",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.160Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 213 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T213",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1161,
        "fields": {
            "title": "算法训练 进制转换",
            "description": r"<br />　　编写一个程序，输入一个二进制的字符串（长度不超过32），然后计算出相应的十进制整数，并把它打印出来。<br /> 　　输入格式：输入为一个字符串，每个字符都是’0’或’1’，字符串的长度不超过32。<br /> 　　输出格式：输出一个整数。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1101",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />13",

            "test_case_id": "2173100991537",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.162Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 217 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T217",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1162,
        "fields": {
            "title": "算法训练 矩阵乘法",
            "description": r"<br />　　输入两个矩阵，分别是m*s，s*n大小。输出两个矩阵相乘的结果。",
            "input_description": r"输入描述:<br />　　第一行，空格隔开的三个正整数m,s,n（均不超过200）。<br /> 　　接下来m行，每行s个空格隔开的整数，表示矩阵A（i，j）。<br /> 　　接下来s行，每行n个空格隔开的整数，表示矩阵B（i，j）。 <br />输入样例: <br />2 3 2<br /> 1 0 -1<br /> 1 1 -3<br /> 0 3<br /> 1 2<br /> 3 1",
            "output_description": r"<br />输出描述: <br />　　m行，每行n个空格隔开的整数，输出相乘後的矩阵C（i，j）的值。<br /> 输出样例: <br />-3 2<br /> -8 2<br /> <br /> <b>提示</b><br /> 矩阵C应该是m行n列，其中C(i,j)等于矩阵A第i行行向量与矩阵B第j列列向量的内积。<br /> 例如样例中C(1,1)=(1,0,-1)*(0,1,3) = 1 * 0 +0*1+(-1)*3=-3<br /> <b> </b>",

            "test_case_id": "2183120252354",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.163Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 218 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T218",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1163,
        "fields": {
            "title": "算法训练 字串统计",
            "description": r"<br />　　给定一个长度为n的字符串S，还有一个数字L，统计长度大于等于L的出现次数最多的子串（不同的出现可以相交），如果有多个，输出最长的，如果仍然有多个，输出第一次出现最早的。",
            "input_description": r"输入描述:<br />　　第一行一个数字L。<br /> 　　第二行是字符串S。<br /> 　　L大于0，且不超过S的长度。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　一行，题目要求的字符串。<br /> <br /> 　　输入样例1：<br /> 　　4<br /> 　　bbaabbaaaaa<br /> <br /> 　　输出样例1：<br /> 　　bbaa<br /> <br /> 　　输入样例2：<br /> 　　2<br /> 　　bbaabbaaaaa<br /> <br /> 　　输出样例2：<br /> 　　aa<br /> 输出样例: <br />",

            "test_case_id": "2193139513171",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　n&lt;=60<br /> 　　S中所有字符都是小写英文字母。",
            "create_time": "2018-02-28T03:15:44.164Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 219 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T219",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1164,
        "fields": {
            "title": "算法训练 字串统计",
            "description": r"<br />　　给定一个长度为n的字符串S，还有一个数字L，统计长度大于等于L的出现次数最多的子串（不同的出现可以相交），如果有多个，输出最长的，如果仍然有多个，输出第一次出现最早的。",
            "input_description": r"输入描述:<br />　　第一行一个数字L。<br /> 　　第二行是字符串S。<br /> 　　L大于0，且不超过S的长度。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　一行，题目要求的字符串。<br /> <br /> 　　输入样例1：<br /> 　　4<br /> 　　bbaabbaaaaa<br /> <br /> 　　输出样例1：<br /> 　　bbaa<br /> <br /> 　　输入样例2：<br /> 　　2<br /> 　　bbaabbaaaaa<br /> <br /> 　　输出样例2：<br /> 　　aa<br /> 输出样例: <br />",

            "test_case_id": "2203158773988",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　n&lt;=60<br /> 　　S中所有字符都是小写英文字母。",
            "create_time": "2018-02-28T03:15:44.165Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 220 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T220",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1165,
        "fields": {
            "title": "算法训练 字符删除",
            "description": r"<br /><b> </b><br /> <b>问题描述</b><br /> 　　编写一个程序，先输入一个字符串str（长度不超过20），再输入单独的一个字符ch，然后程序会把字符串str当中出现的所有的ch字符都删掉，从而得到一个新的字符串str2，然后把这个字符串打印出来。<br /> 　　输入格式：输入有两行，第一行是一个字符串（内部没有空格），第二行是一个字符。<br /> 　　输出格式：经过处理以后的字符串。<br /> <b>输入输出样例</b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />123-45-678<br /> -",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />12345678",

            "test_case_id": "2213178034805",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.166Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 221 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T221",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1167,
        "fields": {
            "title": "算法训练 反置数",
            "description": r"<br />　　一个整数的“反置数”指的是把该整数的每一位数字的顺序颠倒过来所得到的另一个整数。如果一个整数的末尾是以0结尾，那么在它的反置数当中，这些0就被省略掉了。比如说，1245的反置数是5421，而1200的反置数是21。请编写一个程序，输入两个整数，然后计算这两个整数的反置数之和sum，然后再把sum的反置数打印出来。要求：由于在本题中需要多次去计算一个整数的反置数，因此必须把这部分代码抽象为一个函数的形式。<br /> 　　输入格式：输入只有一行，包括两个整数，中间用空格隔开。<br /> 　　输出格式：输出只有一行，即相应的结果。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />435 754",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />199",

            "test_case_id": "2263216556439",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.168Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 226 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T226",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1178,
        "fields": {
            "title": "算法训练 数位分离",
            "description": r"<br />　　编写一个程序，输入一个1000 以内的正整数，然后把这个整数的每一位数字都分离出来，并逐一地显示。<br /> 　　输入格式：输入只有一行，即一个1000以内的正整数。<br /> 　　输出格式：输出只有一行，即该整数的每一位数字，之间用空格隔开。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />769",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />7 6 9",

            "test_case_id": "2443428425426",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.179Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 244 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T244",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1179,
        "fields": {
            "title": "算法训练 薪水计算",
            "description": r"<br />　　编写一个程序，计算员工的周薪。薪水的计算是以小时为单位，如果在一周的时间内，员工工作的时间不超过40 个小时，那么他/她的总收入等于工作时间乘以每小时的薪水。如果员工工作的时间在40 到50 个小时之间，那么对于前40 个小时，仍按常规方法计算；而对于剩余的超额部分，每小时的薪水按1.5 倍计算。如果员工工作的时间超过了50 个小时，那么对于前40 个小时，仍按常规方法计算；对于40～50 个小时之间的部分，每小时的薪水按1.5 倍计算；而对于超出50 个小时的部分，每小时的薪水按2 倍计算。请编写一个程序，输入员工的工作时间和每小时的薪水，然后计算并显示他/她应该得到的周薪。<br /> 　　输入格式：输入只有一行，包括一个整数和一个实数，分别表示工作时间和每小时薪水。<br /> 　　输出格式：输出只有一个实数，表示周薪，保留小数点后2位。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />40 50",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />2000.00",

            "test_case_id": "2453447686243",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.180Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 245 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T245",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1180,
        "fields": {
            "title": "算法训练 整除问题",
            "description": r"<br />　　编写一个程序，输入三个正整数min、max和factor，然后对于min到max之间的每一个整数（包括min和max），如果它能被factor整除，就把它打印出来。<br /> 　　输入格式：输入只有一行，包括三个整数min、max和factor。<br /> 　　输出格式：输出只有一行，包括若干个整数。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1 10 3",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />3 6 9",

            "test_case_id": "2463466947060",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.181Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 246 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T246",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1181,
        "fields": {
            "title": "算法训练 数对",
            "description": r"<br /><b></b><br /> <br /> <b>问题描述</b><br /> 　　编写一个程序，该程序从用户读入一个整数，然后列出所有的数对，每个数对的乘积即为该数。<br /> 　　输入格式：输入只有一行，即一个整数。<br /> 　　输出格式：输出有若干行，每一行是一个乘法式子。（注意：运算符号与数字之间有一个空格）<br /> <b>输入输出样例</b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />32",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />1 * 32 = 32<br /> 2 * 16 = 32<br /> 4 * 8 = 32<br /> 8 * 4 = 32<br /> 16 * 2 = 32<br /> 32 * 1 = 32",

            "test_case_id": "2483486207877",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.182Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 248 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T248",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1182,
        "fields": {
            "title": "算法训练 完数",
            "description": r"<br />　　一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如，6的因子为1、2、3，而6＝1＋2＋3，因此6就是“完数”。又如，28的因子为1、2、4、7、14，而28＝1＋2＋4＋7＋14，因此28也是“完数”。编写一个程序，判断用户输入的一个数是否为“完数”。<br /> 　　输入格式：输入只有一行，即一个整数。<br /> 　　输出格式：输出只有一行，如果该数为完数，输出yes，否则输出no。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />6",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />yes",

            "test_case_id": "2493505468694",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.183Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 249 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T249",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1184,
        "fields": {
            "title": "算法训练 阿尔法乘积",
            "description": r"<br /><b></b>",
            "input_description": r"输入描述:<br />　　计算一个整数的阿尔法乘积。对于一个整数x来说，它的阿尔法乘积是这样来计算的：如果x是一个个位数，那么它的阿尔法乘积就是它本身；否则的话，x的阿尔法乘积就等于它的各位非0的数字相乘所得到的那个整数的阿尔法乘积。例如：4018224312的阿尔法乘积等于8，它是按照以下的步骤来计算的：<br /> 　　4018224312 → 4*1*8*2*2*4*3*1*2 → 3072 → 3*7*2 → 42 → 4*2 → 8<br /> 　　编写一个程序，输入一个正整数（该整数不会超过6,000,000），输出它的阿尔法乘积。<br /> 　　输入格式：输入只有一行，即一个正整数。<br /> 　　输出格式：输出相应的阿尔法乘积。<br /> 　　输入输出样例 <br />输入样例: <br />4018224312",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />8",

            "test_case_id": "2513543990328",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.185Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 251 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T251",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1185,
        "fields": {
            "title": "算法训练 黑色星期五",
            "description": r"<br /><b> </b><br /> <b>问题描述</b><br /> 　　有些西方人比较迷信，如果某个月的13号正好是星期五，他们就会觉得不太吉利，用古人的说法，就是“诸事不宜”。请你编写一个程序，统计出在某个特定的年份中，出现了多少次既是13号又是星期五的情形，以帮助你的迷信朋友解决难题。<br /> 　　说明：（1）一年有365天，闰年有366天，所谓闰年，即能被4整除且不能被100整除的年份，或是既能被100整除也能被400整除的年份；（2）已知1998年1月1日是星期四，用户输入的年份肯定大于或等于1998年。<br /> 　　输入格式：输入只有一行，即某个特定的年份（大于或等于1998年）。<br /> 　　输出格式：输出只有一行，即在这一年中，出现了多少次既是13号又是星期五的情形。<br /> <b>输入输出样例</b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1998",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />3",

            "test_case_id": "2523563251145",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.186Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 252 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T252",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1186,
        "fields": {
            "title": "算法训练 6-3判定字符位置",
            "description": r"<br />　　返回给定字符串s中元音字母的首次出现位置。英语元音字母只有‘a’、‘e’、‘i’、‘o’、‘u’五个。<br /> 　　若字符串中没有元音字母，则返回0。<br /> 　　只考虑小写的情况。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />and",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />1",

            "test_case_id": "2533582511962",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.187Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 253 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T253",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1188,
        "fields": {
            "title": "算法训练 9-7链表数据求和操作",
            "description": r"<br />　　读入10个复数，建立对应链表，然后求所有复数的和。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1 2<br /> 1 3<br /> 4 5<br /> 2 3<br /> 3 1<br /> 2 1<br /> 4 2<br /> 2 2<br /> 3 3<br /> 1 1",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />23+23i",

            "test_case_id": "2563621033596",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-02-28T03:15:44.189Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 256 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T256",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1192,
        "fields": {
            "title": "算法训练 最大体积",
            "description": r"<br />　　每个物品有一定的体积（废话），不同的物品组合，装入背包会战用一定的总体积。假如每个物品有无限件可用，那么有些体积是永远也装不出来的。为了尽量装满背包，附中的OIER想要研究一下物品不能装出的最大体积。题目保证有解，如果是有限解，保证不超过2，000，000，000<br /> 　　如果是无限解，则输出0",
            "input_description": r"输入描述:<br />　　第一行一个整数n（n&lt;=10），表示物品的件数<br /> 　　第2行到N+1行: 每件物品的体积(1&lt;= &lt;=500) <br />输入样例: <br />3<br /> 3<br /> 6<br /> 10",
            "output_description": r"<br />输出描述: <br />　　一个整数ans，表示不能用这些物品得到的最大体积。<br /> 输出样例: <br />17",

            "test_case_id": "2613698076864",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.193Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 261 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T261",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1194,
        "fields": {
            "title": "算法训练 貌似化学",
            "description": r"<br />　　现在有a,b,c三种原料，如果他们按x:y:z混合，就能产生一种神奇的物品d。<br /> 　　当然不一定只产生一份d，但a,b,c的最简比一定是x:y:z<br /> 　　现在给你3种可供选择的物品:<br /> 　　每个物品都是由a,b,c以一定比例组合成的，求出最少的物品数，使得他们能凑出整数个d物品（这里的最少是指三者个数的总和最少）",
            "input_description": r"输入描述:<br />　　第一行三个整数，表示d的配比（x,y,z）<br /> 　　接下来三行，表示三种物品的配比，每行三个整数（&lt;=10000）。 <br />输入样例: <br />3 4 5<br /> 1 2 3<br /> 3 7 1<br /> 2 1 2",
            "output_description": r"<br />输出描述: <br />　　四个整数，分别表示在最少物品总数的前提下a,b,c,d的个数（d是由a,b,c配得的）<br /> 　　目标答案&lt;=10000<br /> 　　如果不存在满足条件的方案，输出NONE<br /> 输出样例: <br />8 1 5 7",

            "test_case_id": "2633736598498",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.195Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 263 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T263",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1196,
        "fields": {
            "title": "算法训练 字符串的展开",
            "description": r"<br />　　在初赛普及组的“阅读程序写结果”的问题中，我们曾给出一个字符串展开的例子：如果在输入的字符串中，含有类似于“d-h”或者“4-8”的字串，我们就把它当作一种简写，输出时，用连续递增的字母获数字串替代其中的减号，即，将上面两个子串分别输出为“defgh”和“45678”。在本题中，我们通过增加一些参数的设置，使字符串的展开更为灵活。具体约定如下：<br /> 　　(1) 遇到下面的情况需要做字符串的展开：在输入的字符串中，出现了减号“-”，减号两侧同为小写字母或同为数字，且按照ASCII码的顺序，减号右边的字符严格大于左边的字符。<br /> 　　(2) 参数p1：展开方式。p1=1时，对于字母子串，填充小写字母；p1=2时，对于字母子串，填充大写字母。这两种情况下数字子串的填充方式相同。p1=3时，不论是字母子串还是数字字串，都用与要填充的字母个数相同的星号“*”来填充。<br /> 　　(3) 参数p2：填充字符的重复个数。p2=k表示同一个字符要连续填充k个。例如，当p2=3时，子串“d-h”应扩展为“deeefffgggh”。减号两边的字符不变。<br /> 　　(4) 参数p3：是否改为逆序：p3=1表示维持原来顺序，p3=2表示采用逆序输出，注意这时候仍然不包括减号两端的字符。例如当p1=1、p2=2、p3=2时，子串“d-h”应扩展为“dggffeeh”。<br /> 　　(5) 如果减号右边的字符恰好是左边字符的后继，只删除中间的减号，例如：“d-e”应输出为“de”，“3-4”应输出为“34”。如果减号右边的字符按照ASCII码的顺序小于或等于左边字符，输出时，要保留中间的减号，例如：“d-d”应输出为“d-d”，“3-1”应输出为“3-1”。",
            "input_description": r"输入描述:<br />　　输入包括两行：<br /> 　　第1行为用空格隔开的3个正整数，一次表示参数p1，p2，p3。<br /> 　　第2行为一行字符串，仅由数字、小写字母和减号“-”组成。行首和行末均无空格。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，为展开后的字符串。<br /> 输出样例: <br />",

            "test_case_id": "2663775120132",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /><table cellspacing=0 cellpadding=2px style='border-collapse:collapse;' class='table table-striped table-horver'><tbody><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'><b>输入</b><br /> </td><td valign=\"top\" style='border:solid 1.0pt'><b>输出</b><br /> </td></tr><tr  style='border:solid 1.0pt'><td valign=\"top\" style='border:solid 1.0pt'>1 2 1<br /> abcs-w1234-9s-4zz<br /> </td><td valign=\"top\" style='border:solid 1.0pt'>abcsttuuvvw1234556677889s-4zz<br /> </td></tr></tbody></table>",
            "create_time": "2018-02-28T03:15:44.197Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 266 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T266",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1201,
        "fields": {
            "title": "算法训练 明明的随机数",
            "description": r"<br />　　明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤100），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。",
            "input_description": r"输入描述:<br />　　输入有2行，第1行为1个正整数，表示所生成的随机数的个数：<br /> 　　N<br /> 　　第2行有N个用空格隔开的正整数，为所产生的随机数。 <br />输入样例: <br />10<br /> 20 40 32 67 40 20 89 300 400 15",
            "output_description": r"<br />输出描述: <br />　　输出也是2行，第1行为1个正整数M，表示不相同的随机数的个数。第2行为M个用空格隔开的正整数，为从小到大排好序的不相同的随机数。<br /> 输出样例: <br />8<br /> 15 20 32 40 67 89 300 400",

            "test_case_id": "2713871424217",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　计13李震摘编自NOIP06PJ01",
            "create_time": "2018-02-28T03:15:44.202Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 271 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T271",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1205,
        "fields": {
            "title": "算法训练 暗恋",
            "description": r"<br />　　同在一个高中，他却不敢去找她，虽然在别人看来，那是再简单不过的事。暗恋，是他唯一能做的事。他只能在每天课间操的时候，望望她的位置，看看她倾心的动作，就够了。操场上的彩砖啊，你们的位置，就是他们能够站立的地方，他俩的关系就像砖与砖之间一样固定，无法动摇。还记得当初铺砖的工人，将整个操场按正方形铺砖（整个操场可视为R行C列的矩阵，矩阵的每个元素为一块正方形砖块），正方形砖块有两种，一种为蓝色，另一种为红色。我们定义他和她之间的“爱情指标”为最大纯色正方形的面积，请你写一个程序求出“爱情指标”。",
            "input_description": r"输入描述:<br />　　第一行两个正整数R和C。<br /> 　　接下来R行C列描述整个操场，红色砖块用1来表示，蓝色砖块用0来表示。 <br />输入样例: <br />5 8<br /> 0 0 0 1 1 1 0 1<br /> 1 1 0 1 1 1 1 1<br /> 0 1 1 1 1 1 0 1<br /> 1 0 1 1 1 1 1 0<br /> 1 1 1 0 1 1 0 1",
            "output_description": r"<br />输出描述: <br />　　一个数，表示他和她之间的“爱情指标”。<br /> 输出样例: <br />9",

            "test_case_id": "2763948467485",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　40%的数据R,C&lt;=10;<br /> 　　70%的数据R,C&lt;=50;<br /> 　　100%的数据R,C&lt;=200;",
            "create_time": "2018-02-28T03:15:44.206Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 276 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T276",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1207,
        "fields": {
            "title": "算法训练 数的统计",
            "description": r"<br />　　在一个有限的正整数序列中，有些数会多次重复出现在这个序列中。<br /> 　　如序列：3，1，2，1，5，1，2。其中1就出现3次，2出现2次，3出现1 次，5出现1次。<br /> 　　你的任务是对于给定的正整数序列，从小到大依次输出序列中出现的数及出现的次数。",
            "input_description": r"输入描述:<br />　　第一行正整数n，表示给定序列中正整数的个数。<br /> 　　第二行是n 个用空格隔开的正整数x，代表给定的序列。 <br />输入样例: <br />12<br /> 8 2 8 2 2 11 1 1 8 1 13 13",
            "output_description": r"<br />输出描述: <br />　　若干行，每行两个用一个空格隔开的数，第一个是数列中出现的数，第二个是该数在序列中出现的次数。<br /> 输出样例: <br />1 3<br /> 2 3<br /> 8 3<br /> 11 1<br /> 13 2",

            "test_case_id": "2783986989119",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　数据：n&lt;=1000；0&lt;x&lt;=1000,000。",
            "create_time": "2018-02-28T03:15:44.208Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 278 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T278",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1210,
        "fields": {
            "title": "算法训练 黑白无常",
            "description": r"<br />　　某寝室的同学们在学术完之后准备玩一个游戏：游戏是这样的，每个人头上都被贴了一张白色或者黑色的纸，现在每个人都会说一句话“我看到x张白色纸条和y张黑色的纸条”，又已知每个头上贴着白色纸的人说的是真话、每个头上贴着黑色纸的人说的是谎话，现在要求你判断哪些人头上贴着的是白色的纸条，如果无解输出“NoSolution.”；如果有多组解，则把每个答案中贴白条的人的编号按照大小排列后组成一个数（比如第一个人和第三个人头上贴着的是白纸条，那么这个数就是13；如果第6、7、8个人都贴的是白纸条，那么这个数就是678）输出最小的那个数（如果全部都是黑纸条也满足情况的话，那么输出0）",
            "input_description": r"输入描述:<br />　　第一行为一个整数n，接下来n行中的第i行有两个整数x和y，分别表示第i个人说“我看到x张白色纸条和y张黑色的纸条”。 <br />输入样例: <br />2<br /> 1 0<br /> 1 0",
            "output_description": r"<br />输出描述: <br />　　一行。如果无解输出“NoSolution.”。否则输出答案中数值（具体见问题描述）最小的那个，如果全部都是黑纸条也满足情况的话，那么输出0<br /> 输出样例: <br />0",

            "test_case_id": "2814044771570",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　n&lt;=8",
            "create_time": "2018-02-28T03:15:44.211Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 281 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T281",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1216,
        "fields": {
            "title": "算法训练 和为T",
            "description": r"<br />　　从一个大小为n的整数集中选取一些元素，使得它们的和等于给定的值T。每个元素限选一次，不能一个都不选。",
            "input_description": r"输入描述:<br />　　第一行一个正整数n，表示整数集内元素的个数。<br /> 　　第二行n个整数，用空格隔开。<br /> 　　第三行一个整数T，表示要达到的和。 <br />输入样例: <br />5<br /> -7 -3 -2 5 9<br /> 0",
            "output_description": r"<br />输出描述: <br />　　输出有若干行，每行输出一组解，即所选取的数字，按照输入中的顺序排列。<br /> 　　若有多组解，优先输出不包含第n个整数的；若都包含或都不包含，优先输出不包含第n-1个整数的，依次类推。<br /> 　　最后一行输出总方案数。<br /> 输出样例: <br />-3 -2 5<br /> -7 -2 9<br /> 2",

            "test_case_id": "2904160336472",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=n&lt;=22<br /> 　　T&lt;=maxlongint<br /> 　　集合中任意元素的和都不超过long的范围",
            "create_time": "2018-02-28T03:15:44.217Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 290 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T290",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1219,
        "fields": {
            "title": "算法训练 友好数",
            "description": r"<br />　　有两个整数，如果每个整数的约数和（除了它本身以外）等于对方，我们就称这对数是友好的。例如：<br /> 　　9的约数和有：1+3=4<br /> 　　4的约数和有：1+2=3<br /> 　　所以9和4不是友好的。<br /> 　　220的约数和有：1 2 4 5 10 11 20 22 44 55 110=284<br /> 　　284的约数和有：1 2 4 71 142=220<br /> 　　所以220和284是友好的。<br /> 　　编写程序，判断两个数是否是友好数。",
            "input_description": r"输入描述:<br />　　一行，两个整数，由空格分隔 <br />输入样例: <br />220 284",
            "output_description": r"<br />输出描述: <br />　　如果是友好数，输出\"yes\"，否则输出\"no\"，注意不包含引号。<br /> 输出样例: <br />yes",

            "test_case_id": "2954218118923",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　两个整数都小于10000",
            "create_time": "2018-02-28T03:15:44.220Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 295 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T295",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1220,
        "fields": {
            "title": "算法训练 连续正整数的和",
            "description": r"<br />　　78这个数可以表示为连续正整数的和，1+2+3，18+19+20+21，25+26+27。<br /> 　　输入一个正整数 n(&lt;=10000)<br /> 　　输出 m 行(n有m种表示法)，每行是两个正整数a，b，表示a+(a+1)+...+b=n。<br /> 　　对于多种表示法，a小的方案先输出。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />78",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />1 12<br /> 18 21<br /> 25 27",

            "test_case_id": "2964237379740",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.221Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 296 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T296",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1221,
        "fields": {
            "title": "算法训练 寂寞的数",
            "description": r"<br />　　道德经曰：一生二，二生三，三生万物。<br /> 　　对于任意正整数n，我们定义d(n)的值为为n加上组成n的各个数字的和。例如，d(23)=23+2+3=28, d(1481)=1481+1+4+8+1=1495。<br /> 　　因此，给定了任意一个n作为起点，你可以构造如下一个递增序列：n,d(n),d(d(n)),d(d(d(n)))....例如，从33开始的递增序列为：<br /> 　　33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...<br /> 　　我们把n叫做d(n)的生成元，在上面的数列中，33是39的生成元，39是51的生成元，等等。有一些数字甚至可以有两个生成元，比如101，可以由91和100生成。但也有一些数字没有任何生成元，如42。我们把这样的数字称为寂寞的数字。",
            "input_description": r"输入描述:<br />　　一行，一个正整数n。 <br />输入样例: <br />40",
            "output_description": r"<br />输出描述: <br />　　按照升序输出小于n的所有寂寞的数字，每行一个。<br /> 输出样例: <br />1<br /> 3<br /> 5<br /> 7<br /> 9<br /> 20<br /> 31",

            "test_case_id": "2984256640557",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　n&lt;=10000",
            "create_time": "2018-02-28T03:15:44.222Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 298 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T298",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1222,
        "fields": {
            "title": "算法训练 学做菜",
            "description": r"<br />　　涛涛立志要做新好青年，他最近在学做菜。由于技术还很生疏，他只会用鸡蛋，西红柿，鸡丁，辣酱这四种原料来做菜，我们给这四种原料标上字母A,B,C,D。<br /> 　　涛涛现在会做的菜有五种：<br /> 　　1、\t西红柿炒鸡蛋 \t 原料：AABDD<br /> 　　2、\t酸辣鸡丁         原料：ABCD<br /> 　　3、\t宫保鸡丁         原料：CCD<br /> 　　4、\t水煮西红柿       原料：BBB<br /> 　　5、\t怪味蛋           原料：AD<br /> 　　这天早上，开开去早市给涛涛买了一些原料回来。由于事先没有什么计划，涛涛决定，对于现存的原料，每次尽量做菜单上靠前（即编号小）的菜。<br /> 　　现在请你写一个程序，判断一下开开和涛涛中午能吃到哪些菜。",
            "input_description": r"输入描述:<br />　　共4个整数a,b,c,d。分别表示开开买的A,B,C,D这4种原料的数量。每种原料不会超过30份。 <br />输入样例: <br />3<br /> 1<br /> 2<br /> 4",
            "output_description": r"<br />输出描述: <br />　　输出5行。其中第i行表示涛涛做的第i种菜的数目。<br /> 输出样例: <br />1<br /> 0<br /> 1<br /> 0<br /> 1",

            "test_case_id": "2994275901374",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.223Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 299 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T299",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1224,
        "fields": {
            "title": "算法训练 猴子分苹果",
            "description": r"<br />　　秋天到了，n只猴子采摘了一大堆苹果放到山洞里，约定第二天平分。这些猴子很崇拜猴王孙悟空，所以都想给他留一些苹果。第一只猴子悄悄来到山洞，把苹果平均分成n份，把剩下的m个苹果吃了,然后藏起来一份，最后把剩下的苹果重新合在一起。这些猴子依次悄悄来到山洞，都做同样的操作，恰好每次都剩下了m个苹果。第二天，这些猴子来到山洞，把剩下的苹果分成n分，巧了，还是剩下了m个。问，原来这些猴子至少采了多少个苹果。",
            "input_description": r"输入描述:<br />　　两个整数，n m <br />输入样例: <br />5 1",
            "output_description": r"<br />输出描述: <br />　　一个整数，表示原来苹果的数目<br /> 输出样例: <br />15621",

            "test_case_id": "3024314423008",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　0&lt;m&lt;n&lt;9",
            "create_time": "2018-02-28T03:15:44.225Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 302 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T302",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1229,
        "fields": {
            "title": "算法训练 A+B problem",
            "description": r"<br />　　Given two integers <i>A</i> and <i>B</i>, your task is to output their sum, <i>A</i>+<i>B</i>.",
            "input_description": r"输入描述:<br />　　The input contains of only one line, consisting of two integers <i>A</i> and <i>B</i>. (0 ≤ A,B ≤ 1 000) <br />输入样例: <br />1 1",
            "output_description": r"<br />输出描述: <br />　　The output should contain only one number that is <i>A</i>+<i>B</i>.<br /> 输出样例: <br />2",

            "test_case_id": "3104410727093",
            "hint": r"HINT:时间限制：1.0s  内存限制：1.0GB<br />",
            "create_time": "2018-02-28T03:15:44.230Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 310 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T310",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1235,
        "fields": {
            "title": "算法训练 王、后传说",
            "description": r"<br />　　地球人都知道，在国际象棋中，后如同太阳，光芒四射，威风八面，它能控制横、坚、斜线位置。<br /> 　　看过清宫戏的中国人都知道，后宫乃步步惊心的险恶之地。各皇后都有自己的势力范围，但也总能找到相安无事的办法。<br /> 　　所有中国人都知道，皇权神圣，伴君如伴虎，触龙颜者死......<br /> 　　现在有一个n*n的皇宫，国王占据他所在位置及周围的共9个格子，这些格子皇后不能使用（如果国王在王宫的边上，占用的格子可能不到9个）。当然，皇后也不会攻击国王。<br /> 　　现在知道了国王的位置（x,y）（国王位于第x行第y列，x,y的起始行和列为1），请问，有多少种方案放置n个皇后，使她们不能互相攻击。",
            "input_description": r"输入描述:<br />　　一行，三个整数，皇宫的规模及表示国王的位置 <br />输入样例: <br />8 2 2",
            "output_description": r"<br />输出描述: <br />　　一个整数，表示放置n个皇后的方案数<br /> 输出样例: <br />10",

            "test_case_id": "3194526291995",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　n&lt;=12",
            "create_time": "2018-02-28T03:15:44.236Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 319 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T319",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1246,
        "fields": {
            "title": "算法训练 水仙花",
            "description": r"<br />　　水仙花数",
            "input_description": r"输入描述:<br />　　判断给定的<b>三位数</b>是否 水仙花 数。所谓 水仙花 数是指其值等于它本身 每位数字立方和的数。例 153 就是一个 水仙花  \t数。 153=1<sup>3</sup>+5<sup>3</sup>+3<sup>3</sup> <br />输入样例: <br />123",
            "output_description": r"<br />输出描述: <br />　　一个整数。<br /> 输出样例: <br />NO",

            "test_case_id": "3344738160982",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　是水仙花数,输出\"YES\",否则输出\"NO\"(不包括引号)",
            "create_time": "2018-02-28T03:15:44.247Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 334 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T334",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1248,
        "fields": {
            "title": "算法训练 特殊的数字四十",
            "description": r"<br />　　特殊的数字四十",
            "input_description": r"输入描述:<br />　　1234是一个非常特殊的四位数，因为它的各位数之和为10，编程求所有这样的四位十进制数。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　按从小到大的顺序输出满足条件的四位十进制数。每个数字占用一行。<br /> 输出样例: <br />",

            "test_case_id": "3384776682616",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.249Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 338 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T338",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1249,
        "fields": {
            "title": "算法训练 Entertaining Geodetics",
            "description": r"<br />　　在此游戏中地图被分为了许多叫作Geo格的正方形方格，其中一些被涂上色，假设没有涂色的为透明色。<br /> 　　地图中还有些Geo符号，它们样子像不同颜色的金字塔（包括透明Geo符号）。每个Geo符号都坐落在Geo格上，每个Geo格上最多一个Geo符号。<br /> 　　Geo符号可以被消除。为了更好地理解Geo符号在消除时发生了什么，这里引入把刚消除的Geo符号放入的队列。<br /> 　　从队列中取出Geo符号，观察包含Geo符号的Geo格的颜色，如果它不是透明的且颜色不同于Geo符号，则把所有这个颜色的Geo格重新涂为Geo符号的颜色（透明的Geo符号则为透明色）。重涂色是在一个无限大的区域从那个有符号的Geo格子开始螺旋状进行的。<br /> 　　<img src=\"/RequireFile.do?fid=452n239E\" width=\"240\" height=\"240\" />.<br /> 　　换句话说，我们选择所有需要重涂色的方格找到它们在以有符号格为中心的无限螺旋表格中所对应的数字。此后按数字的增加顺序我们对其重染色。<br /> 　　如果在重染色时遇到一个格子包含另一个Geo符号的情况则将Geo符号移出并放置在队列尾部。<br /> 　　当重染色结束后Geo符号彻底消失，并且队列中下一个Geo符号（如果有）将取出，重复此操作直至队列为空。<br /> 　　为了更好地理解请看一个例子。<br /> 　　你知道所有格子的颜色、所有符号的位置。计算出队列里符号彻底消失时所造成的重染色次数。<br /> 　　推荐使用I64d输出。",
            "input_description": r"输入描述:<br />　　第一行包含两个数n，m(1&lt;=n，m&lt;=300)—地图的高和宽。<br /> 　　接下来n行每行m个数—格子的颜色。<br /> 　　接下来n行每行m个数—对符号的描述，-1表示没有符号，否则数字代表符号的颜色。<br /> 　　所有颜色都是属于0到10^9的整数，0表示透明。<br /> 　　最后一行两个数x，y(1&lt;=x&lt;=n，1&lt;=y&lt;=m)—需要消除的Geo符号的行和列位置。行从上到下标记，列从左往右标记，从1开始。保证位置(x，y)包含一个符号。 <br />输入样例: <br />5 5<br /> 9 0 1 1 0<br /> 0 0 3 2 0<br /> 1 1 1 3 0<br /> 1 1 1 3 0<br /> 0 1 2 0 3<br /> -1 1 -1 3 -1<br /> -1 -1 -1 0 -1<br /> -1 -1 -1 -1 -1<br /> -1 2 3 -1 -1<br /> -1 -1 -1 -1 2<br /> 4 2",
            "output_description": r"<br />输出描述: <br />　　一行一个数—符号消除时重染色次数。<br /> 输出样例: <br />35",

            "test_case_id": "3394795943433",
            "hint": r"HINT:时间限制：2.0s  内存限制：256.0MB<br /><img src=\"/RequireFile.do?fid=nMytgBA9\" width=\"170\" height=\"220\" />",
            "create_time": "2018-02-28T03:15:44.250Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 339 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T339",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1254,
        "fields": {
            "title": "算法训练 Don't fear, DravDe is kind",
            "description": r"<br />　　这一天，有一列车子排起了一排长队，必经之路是一个被魔王笼罩的山洞。每辆车的司机害怕魔王程度不同，所以每个司机有一些要求。<br /> 　　车子有n台，排成一条长队，每辆车有4个属性:<br /> 　　V  ——这辆车的总价值，价值就是比如它其中的乘客和货物的价值<br /> 　　c  ——这辆车里面的人数量（司机表示自己也算一个乘客，司机和乘客不用区分开来）<br /> 　　l  ——在这辆车的前面需要总量正好为多少乘客的车（不多也不少），这车才敢开<br /> 　　r  ——在这辆车的后面需要总量正好为多少乘客的车（不多也不少），这车才敢开<br /> 　　“前面需要总量正好为多少乘客的车”指的是驶在这辆车前面所有的车的乘客总数。<br /> 　　“后面需要总量正好为多少乘客的车”指的是驶在这辆车后面所有的车的乘客总数。<br /> 　　你不能改变每辆车在车队的相对顺序，但你可以安排某些车退出车队，保证依然在车队的每辆车都敢开了，即满足上述条件，并且剩下车的v的总量最大。<br /> 　　-----------------------------<br /> 　　简单来说，给您按输入顺序排列的n辆车，您需要删去里面的一些车（剩下的车仍然按原相对顺序排列）。<br /> 　　使得对于每辆车，若它没被删去，设其为输入的第i辆车，<br /> 　　要满足<br /> 　　l[i]= sigma{c[j] | j&lt;i 且第j辆车没被删去}<br /> 　　r[i]= sigma{c[j] | j&gt;i 且第j辆车没被删去}<br /> 　　在满足这些条件前提下，要求sigma{V[i] | i没被删去} 最大，<br /> 　　请输出这个最大值，并且递增输出没有被删去的车的标号。",
            "input_description": r"输入描述:<br />　　输入的第一行为一个正整数n（1&lt;=n&lt;=10^5）——车的个数。<br /> 　　接下来n行，每行四个整数，第i行的数字: vi, ci,li ,r<sub>i</sub> ,（1&lt;=vi&lt;=10^4 , 1&lt;=ci&lt;=10^5,0&lt;=li,ri&lt;=10^5），车子们从1开始编号，从车队的最前头开始算起。 <br />输入样例: <br />5<br /> 1 1 0 3<br /> 1 1 1 2<br /> 1 1 2 1<br /> 1 1 3 0<br /> 2 1 3 0",
            "output_description": r"<br />输出描述: <br />　　第一行输出一个数k：会继续在这车队里的车的总数（注意我们的目标是让价值最大）。<br /> 　　第二行k个数，递增输出继续在车队里的车的编号。<br /> 　　请留心你不允许改变车的次序。如果答案不唯一，输出任意一个。<br /> 输出样例: <br />4<br /> 1 2 3 5",

            "test_case_id": "3464892247518",
            "hint": r"HINT:时间限制：2.0s  内存限制：256.0MB<br />　　对于20%的数据，n&lt;=100<br /> 　　对于50%的数据，n&lt;=1000<br /> 　　对于100%的数据，n&lt;=100000<br /> 　　对于100%的数据，1&lt;=vi&lt;=10^4 , 1&lt;=ci&lt;=10^5,0&lt;=li,ri&lt;=10^5",
            "create_time": "2018-02-28T03:15:44.255Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 346 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T346",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1261,
        "fields": {
            "title": "算法训练 Buying Sets",
            "description": r"<br />　　给定n个集合, 要求选出其中某些集合, 使得这些集合的并集的势, 等于选出的集合的数目.<br /> 　　对于任意的k(1&lt;=k&lt;=n), 满从中选出任意k个集合, 这k个集合的并集的势一定大于等于k.<br /> 　　每个集合有一个权值, 每个选择方案的代价是所选的集合的权值的和.<br /> 　　请输出代价最小的选择方案的代价.<br /> 　　当然, 不选择任何一个集合是一个可行的方案(权值和为0), 但不一定最优(权值和可以为负).",
            "input_description": r"输入描述:<br />　　第一行一个正整数n(1&lt;=n&lt;=300), 为集合个数.<br /> 　　在接下来n行中, 第i行描述第i个集合:<br /> 　　首先给出一个正整数m[i]为该集合的势, 显然1&lt;=m[i]&lt;=n.<br /> 　　接下来m[i]个在1到n之间的整数, 表示该集合中的元素.<br /> 　　最后一行n个整数, 为每个集合的权值, 绝对值不超过1e6. <br />输入样例: <br />3<br /> 1 1<br /> 2 2 3<br /> 1 3<br /> 10 20 -3",
            "output_description": r"<br />输出描述: <br />　　仅一个整数, 为代价最小的选择方案的代价.<br /> 输出样例: <br />-3",

            "test_case_id": "3555027073237",
            "hint": r"HINT:时间限制：2.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.262Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 355 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T355",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1262,
        "fields": {
            "title": "算法训练 Representative Sampling (30_points)",
            "description": r"<br /><b>【题目描述】</b><br /> 　　来自ABBYY的小明有一个与“细胞与遗传学研究所”的合作。最近，研究所用一个新的题目考验小明。题目如下。<br /> 　　有由n个细胞组成的一个集合（不一定不同）每个细胞是一个由小写拉丁字母组成的字符串。科学家给小明提出的问题是从给定集合中选出一个大小为k的子集，使得所选子集的代表值最大。<br /> 　　小明做了些研究并得出了一个结论，即一个蛋白质集合的代表制可以用一个方便计算的整数来表示。我们假设当前的集合为{<i>a</i><sub>1</sub>,&thinsp;...,&thinsp;<i>a<sub>k</sub></i>}，包含了k个用以表示蛋白质的字符串。那么蛋白质集合的代表值可以用如下的式子来表示：<br /> <br /> 　　其中<i>f</i>(<i>x</i>,&thinsp;<i>y</i>)表示字符串<i>x</i>和<i>y</i>的最长公共前缀的长度，例如：<br /> 　　<i>f</i>(\"abc\", \"abd\")&thinsp;=&thinsp;2  ， <i>f</i>(\"ab\", \"bcd\")&thinsp;=&thinsp;0.<br /> 　　因此，蛋白质集合{\"abc\", \"abd\", \"abe\"}的代表值等于6，集合{\"aaa\", \"ba\", \"ba\"}的代表值等于2。<br /> 　　在发现了这个之后，小明要求赛事参与者写一个程序选出，给定蛋白质的集合中的大小为k的子集中，能获得最大可能代表性值得一个子集。帮助他解决这个问题吧！<br /> <b>【输入格式】</b><br /> 　　输入数据第一行包含2个正整数n和k（1≤<i>k</i>≤<i>n</i>），由一个空格隔开。接下来的n行每一行都包含对蛋白质的描述。每个蛋白质都是一个仅有不超过500个小写拉丁字母组成的非空字符串。有些字符串可能是相等的。",
            "input_description": r"输入描述:<br />　　输出一个整数，表示给定蛋白质集合的大小为k的子集的代表值最大可能是多少。<br /> <br /> <b>【数据规模】</b><br /> 　　20%的数据保证：1&thinsp;≤&thinsp;<i>n</i>&thinsp;≤&thinsp;20<br /> 　　50%的数据保证：1&thinsp;≤&thinsp;<i>n</i>&thinsp;≤&thinsp;100<br /> 　　100%的数据保证：1&thinsp;≤&thinsp;<i>n</i>&thinsp;≤&thinsp;2000<br /> <br /> <b>【样例输入1】</b><br /> 　　3 2<br /> 　　aba<br /> 　　bzd<br /> 　　abq<br /> <b>【样例输出1】</b><br /> 　　2<br /> <br /> <b>【样例输入2】</b><br /> 　　4 3<br /> 　　eee<br /> 　　rrr<br /> 　　ttt<br /> 　　qqq<br /> <b>【样例输出2】</b><br /> 　　0<br /> <b>【样例输入3】</b><br /> 　　4 3<br /> 　　aaa<br /> 　　abba<br /> 　　abbc<br /> 　　abbd<br /> <b>【样例输出3】</b><br /> 　　9 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3575046334054",
            "hint": r"HINT:时间限制：2.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.263Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 357 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T357",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1269,
        "fields": {
            "title": "算法训练 s01串",
            "description": r"<br />　　s01串初始为\"0\"<br /> 　　按以下方式变换<br /> 　　0变1，1变01",
            "input_description": r"输入描述:<br />　　1个整数(0~19) <br />输入样例: <br />3",
            "output_description": r"<br />输出描述: <br />　　n次变换后s01串<br /> 输出样例: <br />101",

            "test_case_id": "3665181159773",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　0~19",
            "create_time": "2018-02-28T03:15:44.270Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 366 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T366",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1272,
        "fields": {
            "title": "算法训练 P1101",
            "description": r"<br />　　<br /> 　　有一份提货单，其数据项目有：商品名（MC）、单价（DJ）、数量（SL）。定义一个结构体prut，其成员是上面的三项数据。在主函数中定义一个prut类型的结构体数组，输入每个元素的值，计算并输出提货单的总金额。<br /> 　　输入格式：第一行是数据项个数N(N&lt;100)，接下来每一行是一个数据项。商品名是长度不超过100的字符串，单价为double类型，数量为整型。<br /> 　　输出格式：double类型的总金额。<br /> <b>输入：</b><br /> 　　4<br /> 　　book 12.5 3<br /> 　　pen 2.5 10<br /> 　　computer 3200 1<br /> 　　flower 47 5<br /> <br /> <b>输出：</b><br /> 　　3497.500000",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3705238942224",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.273Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 370 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T370",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1273,
        "fields": {
            "title": "算法训练 P1102",
            "description": r"<br />　　定义一个学生结构体类型student，包括4个字段，姓名、性别、年龄和成绩。然后在主函数中定义一个结构体数组（长度不超过1000），并输入每个元素的值，程序使用冒泡排序法将学生按照成绩从小到大的顺序排序，然后输出排序的结果。<br /> 　　输入格式：第一行是一个整数N（N&lt;1000），表示元素个数；接下来N行每行描述一个元素，姓名、性别都是长度不超过20的字符串，年龄和成绩都是整型。<br /> 　　输出格式：按成绩从小到大输出所有元素，若多个学生成绩相同则成绩相同的同学之间保留原来的输入顺序。<br /> <b>输入：</b><br /> 　　3<br /> 　　Alice female 18 98<br /> 　　Bob male 19 90<br /> 　　Miller male 17 92<br /> <br /> <b>输出：</b><br /> 　　Bob male 19 90<br /> 　　Miller male 17 92<br /> 　　Alice female 18 98<br /> <b> </b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3715258203041",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-02-28T03:15:44.274Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 371 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T371",
            "tags": [
                4
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1020,
        "fields": {
            "title": "算法提高 两条直线",
            "description": r"<br /> \t<p>给定平面上n个点。</p> \t<p>求两条直线，这两条直线互相垂直，而且它们与x轴的夹角为45度，并且n个点中离这两条直线的曼哈顿距离的最大值最小。</p> \t<p>两点之间的曼哈顿距离定义为横坐标的差的绝对值与纵坐标的差的绝对值之和，一个点到两条直线的曼哈顿距离是指该点到两条直线上的所有点的曼哈顿距离中的最小值。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行包含一个数n。</p> \t<p>接下来n行，每行包含两个整数，表示n个点的坐标（横纵坐标的绝对值小于10<sup>9</sup>）。</p>  <br />输入样例: <br /> 4<br /> 1 0<br /> 0 1<br /> 2 1<br /> 1 2 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个值，表示最小的最大曼哈顿距离的值，保留一位小数。 <br /> 输出样例: <br /> 1.0 \t",

            "test_case_id": "19385216340",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于30%的数据，n&lt;=100。</p> <p>对于另外30%的数据，坐标范的绝对值小于100。</p> <p>对于100%的数据，n&lt;=10<sup>5</sup>。</p> ",
            "create_time": "2018-03-28T03:15:44.21Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 19 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T19",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1021,
        "fields": {
            "title": "算法提高 矩阵翻转",
            "description": r"<br /> \t<p>Ciel有一个N*N的矩阵，每个格子里都有一个整数。</p> \t<p>N是一个奇数，设X = (N+1)/2。Ciel每次都可以做这样的一次操作：他从矩阵选出一个X*X的子矩阵，并将这个子矩阵中的所有整数都乘以-1。</p> \t<p>现在问你经过一些操作之后，矩阵中所有数的和最大可以为多少。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行为一个正整数N。</p> \t<p>接下来N行每行有N个整数，表示初始矩阵中的数字。每个数的绝对值不超过1000。</p>  <br />输入样例: <br /> 3<br /> -1 -1 1<br /> -1 1 -1<br /> 1 -1 -1 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数，表示操作后矩阵中所有数之和的最大值。 <br /> 输出样例: <br /> 9 \t",

            "test_case_id": "20404477157",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t<p>1 &lt;= N &lt;= 33，且N为奇数。</p> ",
            "create_time": "2018-03-28T03:15:44.22Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 20 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T20",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1022,
        "fields": {
            "title": "算法提高 金属采集",
            "description": r"<br /> \t<p>人类在火星上发现了一种新的金属！这些金属分布在一些奇怪的地方，不妨叫它节点好了。一些节点之间有道路相连，所有的节点和道路形成了一棵树。一共有 n 个节点，这些节点被编号为 1~n 。人类将 k 个机器人送上了火星，目的是采集这些金属。这些机器人都被送到了一个指定的着落点， S 号节点。每个机器人在着落之后，必须沿着道路行走。当机器人到达一个节点时，它会采集这个节点蕴藏的所有金属矿。当机器人完成自己的任务之后，可以从任意一个节点返回地球。当然，回到地球的机器人就无法再到火星去了。我们已经提前测量出了每条道路的信息，包括它的两个端点 x 和 y，以及通过这条道路需要花费的能量 w 。我们想花费尽量少的能量采集所有节点的金属，这个任务就交给你了。</p> ",
            "input_description": r"输入描述:<br /> \t<p>第一行包含三个整数 n, S 和 k ，分别代表节点个数、着落点编号，和机器人个数。</p> \t<p>接下来一共 n-1 行，每行描述一条道路。一行含有三个整数 x, y 和 w ，代表在 x 号节点和 y 号节点之间有一条道路，通过需要花费 w 个单位的能量。所有道路都可以双向通行。</p>  <br />输入样例: <br /> 6 1 3<br /> 1 2 1<br /> 2 3 1<br /> 2 4 1000<br /> 2 5 1000<br /> 1 6 1000 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个整数，代表采集所有节点的金属所需要的最少能量。 <br /> 输出样例: <br /> 3004 \t",

            "test_case_id": "21423737974",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t<p>所有机器人在 1 号节点着陆。</p> \t<p>第一个机器人的行走路径为 1-&gt;6 ，在 6 号节点返回地球，花费能量为1000。</p> \t<p>第二个机器人的行走路径为 1-&gt;2-&gt;3-&gt;2-&gt;4 ，在 4 号节点返回地球，花费能量为1003。</p> \t<p>第一个机器人的行走路径为 1-&gt;2-&gt;5 ，在 5 号节点返回地球，花费能量为1001。</p> ",
            "create_time": "2018-03-28T03:15:44.23Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 21 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T21",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1023,
        "fields": {
            "title": "算法提高 道路和航路",
            "description": r"<br /> <p>农夫约翰正在针对一个新区域的牛奶配送合同进行研究。他打算分发牛奶到T个城镇（标号为1..T），这些城镇通过R条标号为（1..R）的道路和P条标号为（1..P）的航路相连。</p> <p>每一条公路i或者航路i表示成连接城镇A<sub>i</sub>（1&lt;=A_i&lt;=T）和B<sub>i</sub>（1&lt;=B<sub>i</sub>&lt;=T）代价为C<sub>i</sub>。每一条公路，C<sub>i</sub>的范围为0&lt;=C<sub>i</sub>&lt;=10,000；由于奇怪的运营策略，每一条航路的C<sub>i</sub>可能为负的，也就是-10,000&lt;=C<sub>i</sub>&lt;=10,000。</p> <p>每一条公路都是双向的，正向和反向的花费是一样的，都是非负的。</p> <p>每一条航路都根据输入的A<sub>i</sub>和B<sub>i</sub>进行从A<sub>i</sub>-&gt;B<sub>i</sub>的单向通行。实际上，如果现在有一条航路是从A<sub>i</sub>到B<sub>i</sub>的话，那么意味着肯定没有通行方案从B<sub>i</sub>回到A<sub>i</sub>。</p> <p>农夫约翰想把他那优良的牛奶从配送中心送到各个城镇，当然希望代价越小越好，你可以帮助他嘛？配送中心位于城镇S中（1<=S<=T）。</p>  ",
            "input_description": r"输入描述:<br /> \t<p>输入的第一行包含四个用空格隔开的整数T，R，P，S。</p> \t<p>接下来R行，描述公路信息，每行包含三个整数，分别表示A<sub>i</sub>，B<sub>i</sub>和C<sub>i</sub>。</p> \t<p>接下来P行，描述航路信息，每行包含三个整数，分别表示A<sub>i</sub>，B<sub>i</sub>和C<sub>i</sub>。</p>  <br />输入样例: <br /> 6 3 3 4<br /> 1 2 5<br /> 3 4 5<br /> 5 6 10<br /> 3 5 -100<br /> 4 6 -100<br /> 1 3 -10 ",
            "output_description": r"<br />输出描述: <br /> \t输出T行，分别表示从城镇S到每个城市的最小花费，如果到不了的话输出NO PATH。 <br /> 输出样例: <br /> NO PATH<br /> NO PATH<br /> 5<br /> 0<br /> -95<br /> -100 \t",

            "test_case_id": "22442998791",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>对于20%的数据，T&lt;=100，R&lt;=500，P&lt;=500；</p> <p>对于30%的数据，R&lt;=1000，R&lt;=10000，P&lt;=3000；</p> <p>对于100%的数据，1&lt;=T&lt;=25000，1&lt;=R&lt;=50000，1&lt;=P&lt;=50000。</p> ",
            "create_time": "2018-03-28T03:15:44.24Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 22 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T22",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1024,
        "fields": {
            "title": "算法提高 最小方差生成树",
            "description": r"<br />     给定带权无向图，求出一颗方差最小的生成树。 ",
            "input_description": r"输入描述:<br />    输入多组测试数据。第一行为N,M，依次是点数和边数。接下来M行，每行三个整数U,V,W，代表连接U,V的边，和权值W。保证图连通。n=m=0标志着测试文件的结束。    <br />输入样例: <br /> 4 5<br /> 1 2 1<br /> 2 3 2<br /> 3 4 2<br /> 4 1 1<br /> 2 4 3<br /> 4 6<br /> 1 2 1<br /> 2 3 2<br /> 3 4 3<br /> 4 1 1<br /> 2 4 3<br /> 1 3 3<br /> 0 0  ",
            "output_description": r"<br />输出描述: <br />     对于每组数据，输出最小方差，四舍五入到0.01。输出格式按照样例。 <br /> 输出样例: <br /> Case 1: 0.22<br /> Case 2: 0.00 \t",

            "test_case_id": "23462259608",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> <p>1&lt;=U,V&lt;=N&lt;=50,N-1&lt;=M&lt;=1000,0&lt;=W&lt;=50。数据不超过5组。</p> ",
            "create_time": "2018-03-28T03:15:44.25Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 23 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T23",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1046,
        "fields": {
            "title": "算法提高 邮票面值设计",
            "description": r"<br />　　给定一个信封，最多只允许粘贴N张邮票，计算在给定K（N+K≤13）种邮票的情况下（假定所有的邮票数量都足够），如何设计邮票的面值，能得到最大值MAX，使在1～MAX之间的每一个邮资值都能得到。<br /> <br /> 　　例如，N=3，K=2，如果面值分别为1分、4分，则在1分～6分之间的每一个邮资值都能得到（当然还有8分、9分和12分）；如果面值分别为1分、3分，则在1分～7分之间的每一个邮资值都能得到。可以验证当N=3，K=2时，7分就是可以得到的连续的邮资最大值，所以MAX=7，面值分别为1分、3分。",
            "input_description": r"输入描述:<br />　　一行，两个数N、K <br />输入样例: <br />3 2",
            "output_description": r"<br />输出描述: <br />　　两行，第一行升序输出设计的邮票面值，第二行输出“MAX=xx”（不含引号），其中xx为所求的能得到的连续邮资最大值。<br /> 输出样例: <br />1 3<br /> MAX=7",

            "test_case_id": "45885997582",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.47Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 45 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T45",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1081,
        "fields": {
            "title": "算法提高 子集选取",
            "description": r"<br />　　一个有N个元素的集合有2^N个不同子集（包含空集），现在要在这2^N个集合中取出若干集合（至少一个），使得它们的交集的元素个数为K，求取法的方案数，答案模1000000007。",
            "input_description": r"输入描述:<br />　　输入一行两个整数N，K。 <br />输入样例: <br />3 2",
            "output_description": r"<br />输出描述: <br />　　输出一个整数表示答案。<br /> 输出样例: <br />6",

            "test_case_id": "801560126177",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1 &lt;= K &lt;= N &lt;= 10 ^ 6。",
            "create_time": "2018-03-28T03:15:44.82Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 80 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T80",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1082,
        "fields": {
            "title": "算法提高 冒泡排序计数",
            "description": r"<br />　　考虑冒泡排序的一种实现。<br /> 　　bubble-sort (A[], n)<br /> 　　&gt; round = 0<br /> 　　&gt; while A is not sorted<br /> 　　&gt; &gt; round := round + 1<br /> 　　&gt; &gt; for i := 1 to n - 1<br /> 　　&gt; &gt; &gt; if (A[i] &gt; A[i + 1])<br /> 　　&gt; &gt; &gt; &gt; swap(A[i], A[i + 1])<br /> 　　求1 .. n的排列中，有多少个排列使得A被扫描了K遍，亦即算法结束时round == K。<br /> <br /> 　　答案模20100713输出。",
            "input_description": r"输入描述:<br />　　输入包含多组数据。每组数据为一行两个整数N，K。 <br />输入样例: <br />3<br /> 3 0<br /> 3 1<br /> 3 2",
            "output_description": r"<br />输出描述: <br />　　对每组数据，输出一行一个整数表示答案。<br /> 输出样例: <br />1<br /> 3<br /> 2",

            "test_case_id": "811579386994",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　T &lt;= 10 ^ 5。<br /> 　　1 &lt;= K &lt; N &lt; 10 ^ 6。",
            "create_time": "2018-03-28T03:15:44.83Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 81 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T81",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1108,
        "fields": {
            "title": "算法提高 递归倒置字符数组",
            "description": r"<br />　　完成一个递归程序，倒置字符数组。并打印实现过程<br /> 　　递归逻辑为：<br /> 　　当字符长度等于1时，直接返回<br /> 　　否则，调换首尾两个字符，在递归地倒置字符数组的剩下部分",
            "input_description": r"输入描述:<br />　　字符数组长度及该数组 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　在求解过程中，打印字符数组的变化情况。<br /> 　　最后空一行，在程序结尾处打印倒置后该数组的各个元素。<br /> 输出样例: <br />",

            "test_case_id": "1122080168236",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.109Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 112 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T112",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1109,
        "fields": {
            "title": "算法提高 立方体截断问题",
            "description": r"<br />　　如右图所示，这是一个空心正方体（请想象用纸糊出来的正方体），每条棱的编号如图所示<br /> 　　(图在http://166.111.138.150/fop/attach/cube.jpg)。<br /> <br /> 　　考虑剪开若干条棱，请判断正方体是否会被剪成分开（即判断正方体是否会被分割成不少于2个部分）。",
            "input_description": r"输入描述:<br />　　本题包括多组数据。<br /> 　　第一行输入一个N，表示数据组数。<br /> 　　对于每一组数据，都包括两行。<br /> 　　第一行输入一个n，表示总共剪开了n条棱。<br /> 　　第二行有n个数，每个数表示剪开的棱的编号。（输入保证每条棱出现次数不超过1） <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　对于每一组输入，输出一行。<br /> 　　若正方体会被分割成不少于2个部分，则输出“Yes”，否则输出“No”（均不包括引号）。<br /> 输出样例: <br />",

            "test_case_id": "1272099429053",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.110Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 127 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T127",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1111,
        "fields": {
            "title": "算法提高 Torry的困惑(提高型)",
            "description": r"<br />　　Torry从小喜爱数学。一天，老师告诉他，像2、3、5、7……这样的数叫做质数。Torry突然想到一个问题，前10、100、1000、10000……个质数的乘积是多少呢？他把这个问题告诉老师。老师愣住了，一时回答不出来。于是Torry求助于会编程的你，请你算出前n个质数的乘积。不过，考虑到你才接触编程不久，Torry只要你算出这个数模上50000的值。",
            "input_description": r"输入描述:<br />　　仅包含一个正整数n，其中n&lt;=100000。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出一行，即前n个质数的乘积模50000的值。<br /> 输出样例: <br />",

            "test_case_id": "1302137950687",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.112Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 130 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T130",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1113,
        "fields": {
            "title": "算法提高 计算时间",
            "description": r"<br />　　给定一个t，将t秒转化为HH:MM:SS的形式，表示HH小时MM分钟SS秒。HH,MM,SS均是两位数，如果小于10用0补到两位。",
            "input_description": r"输入描述:<br />　　第一行一个数T(1&lt;=T&lt;=100,000)，表示数据组数。后面每组数据读入一个数t，0&lt;=t&lt;24*60*60。 <br />输入样例: <br />2<br /> 0<br /> 86399",
            "output_description": r"<br />输出描述: <br />　　每组数据一行，HH:MM:SS。<br /> 输出样例: <br />00:00:00<br /> 23:59:59",

            "test_case_id": "1322176472321",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.114Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 132 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T132",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1114,
        "fields": {
            "title": "算法提高 最小乘积(提高型)",
            "description": r"<br />　　给两组数，各n个。<br /> 　　请调整每组数的排列顺序，使得两组数据相同下标元素对应相乘，然后相加的和最小。要求程序输出这个最小值。<br /> 　　例如两组数分别为:1 3　　-5和-2 4 1<br /> <br /> 　　那么对应乘积取和的最小值应为：<br /> 　　(-5) * 4 + 3 * (-2) + 1 * 1 = -25",
            "input_description": r"输入描述:<br />　　第一个行一个数T表示数据组数。后面每组数据，先读入一个n，接下来两行每行n个数，每个数的绝对值小于等于1000。<br /> 　　n&lt;=1000,T&lt;=10 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　一个数表示答案。<br /> 输出样例: <br />",

            "test_case_id": "1342195733138",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.115Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 134 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T134",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1115,
        "fields": {
            "title": "算法提高 卡勒沃夫之弱水路三千(提高型)",
            "description": r"<br />　　锦瑟年华谁与度 莫问情归处 只影向斜阳 剑吼西风 欲把春留驻<br /> 　　天涯芳草无归路 回首花无数 解语自销魂 弱袂萦春 尘缘不相误<br /> 　　......<br /> 　　在卡勒沃夫充满文学杀伤力的声音中，身处紫荆2号楼202B的四位远近高低各不同的室友纷纷回忆起了各自波澜起伏的过去，并对长在百草园，邻有百花谷的现状表达了各自的见解。<br /> 　　某Q：\"...我小学就开窍了...她的父母说我很好，但是...今天又和北林的联系了...\"<br /> 　　某X：\"...差点就成了，结果到学校了...这个方法放假了我去对我的同桌用！...\"<br /> 　　某W：\"...\"（千言万语不言中，有大量的故事等待考古）<br /> 　　某Z：\"...为了来清华...咱们审美观不一样，不会抢...\"<br /> 　　......<br /> 　　卡勒沃夫在这个不朽的夜话中搜集出了某人零散的历任女友资料，为了强迫某人将他出的题目的标程交出，现在卡勒沃夫需要一个能将这些零散信息整合起来的程序。伴随着雄壮委婉动人的音乐，身为程序设计快男（超女）的你降临了！卡勒沃夫正对着您做Orz状并请求着：\"神牛啊~请施舍给我一段程序把~偶米头发~\"。。",
            "input_description": r"输入描述:<br />　　第一行为一个不超过5的整数T，表示数据的组数。之后每组数据的一行为一个不超过100的整数n。之后n行每行有两个用单个空格隔开的字符串（每个字符串只有英文大小写字母，长度不超过10），为两位mm的名字。每行第一个mm先于第二个mm成为某人的女友。<br /> 　　在这里我们假装诅咒某人不会同时被两个或两个以上mm泡，某个mm抛弃了某人后不会再吃回头草，同时卡勒沃夫深邃的洞察力使得他收集到了充足的信息以确定某人女友的先后顺序。<br /> 　　在小数据组中出现的人物不超过13个 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出T行，每行对应一组数据，并按照mm们从先到后成为某人女友的顺序输出她们的名字，各个名字间用一个空格隔开。<br /> 输出样例: <br />",

            "test_case_id": "1352214993955",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.116Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 135 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T135",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1116,
        "fields": {
            "title": "算法提高 和最大子序列",
            "description": r"<br />　　对于一个给定的长度为N的整数序列A，它的“子序列”的定义是：A中非空的一段连续的元素（整数）。你要完成的任务是，在所有可能的子序列中，找到一个子序列，该子序列中所有元素的和是最大的（跟其他所有子序列相比）。程序要求你输出这个最大值。",
            "input_description": r"输入描述:<br />　　输入文件的第一行包含一个整数N，第二行包含N个整数，表示A。<br /> 　　其中<br /> 　　1 &lt;= N &lt;= 100000<br /> 　　-10000 &lt;= A[i] &lt;=　　10000 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出仅包含一个整数，表示你算出的答案。<br /> 输出样例: <br />",

            "test_case_id": "1372234254772",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.117Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 137 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T137",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1119,
        "fields": {
            "title": "算法提高 统计单词数",
            "description": r"<br />　　统计输入英文文章段落中不同单词（单词有大小写之分,　　但统计时忽略大小写）各自出现的次数。 输入段落中所含单词的总数不超过100，最长单词的长度不超过20个字母.",
            "input_description": r"输入描述:<br />　　一个包含若干句子的段落, 每个句子由若干英文单词组成. 除空格,　　逗号和句号外, 这些输入的句子中不含其他非字母字符, 并且, 逗号和句号紧跟在它前面的英文单词后面, 中间没有空格. 段落最后一个字符是回车符,　　表示输入结束. <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　若段落中共有M个不同的英文单词，则按照其在段落中出现的先后顺序输出M行，各行的格式为:　　单词中所有字母均用大写形式输出（最长的单词顶格输出，它前面没有多余的空格;　　其余单词与其右对齐）+冒号+N个*号+该单词在段落中的出现次数N<br /> 输出样例: <br />",

            "test_case_id": "1402292037223",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.120Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 140 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T140",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1121,
        "fields": {
            "title": "算法提高 实数相加",
            "description": r"<br />　　计算两个实数相加的结果。<br /> 　　输入的实数满足如下要求: (1)　　小数点前的整数部分最多100位，(2) 小数点后的小数部分最多100位.",
            "input_description": r"输入描述:<br />　　两行字符串，每行都是一个合法的实数。合法的意思是指:　　整数部分的值如果大于零,则最高位数字必定大于零. 如果整数部分的值为零,则整数部分只有一个零. 小数部分尾部可以有任意多的零. 可以没有小数部分,　　此时也没有小数点. 如果有小数点, 则至少需要有一位小数部分, 且允许是零. <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　相加结果。注意: 小数部分末尾如果有连续的0, 则它们都是有效数字,　　不能舍去. 如果是两个整数相加, 则结果仍为整数而没有小数部分.<br /> 输出样例: <br />",

            "test_case_id": "1422330558857",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.122Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 142 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T142",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1122,
        "fields": {
            "title": "算法提高 项链",
            "description": r"<br />　　由 n(1≤n≤100)　　个珠子组成的一个项链，珠子有红、蓝、白三种颜色，各种颜色的珠子的安排顺序由键盘输入的字符串任意给定。蓝色用小写字母b表示,红色用小写字母r表示,　　白色用小写字母w表示.<br /> <br /> 　　假定从项链的某处将其剪断，把它摆成一条直线。先从左端向右收集同色珠子，遇到第一个异色珠子时停止.　　收集过程中, 白色是一种特殊颜色, 既可以看成红色也可以看成蓝色。然后再从剩余珠子的右端向左重复上述过程。<br /> <br /> 　　例如：对下图一所示的项链, 如果从图一中标记的位置0处剪断,　　则按顺时针顺序得到wbbbwwrrbwbrrwb（如图二所示）。这时从左端开始收集可以得到wbbbww,　　共6个珠子；然后从剩余珠子右端开始收集得到wb，共2个珠子。这种剪法共可收集到6+2=8个珠子。 如果从图一中标记的位置4处剪断,　　则按顺时针顺序得到wwrrbwbrrwbwbbb（如图二所示）。这时从左端收集可以得到wwrr,共4个珠子；然后从剩余珠子右端收集可以得到wbwbbb，共6个珠子。这种剪法共可收集到4+6=10个珠子。<br /> <br /> 　　要求: 在项链中选择合适的剪断位置, 使得从左右两端收集到的珠子数目之和最大，输出收集到的珠子数的最大值M。<br /> <img height=500 src=\"\" /><br /> <img height=280 src=\"\" />",
            "input_description": r"输入描述:<br />　　由小写字母b,r,w组成的字符串。此字符串记录了一个首尾相接的项链从某处断开后，按顺时针顺序得到的珠子的直线排列。 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　收集到的珠子数的最大值 M<br /> 输出样例: <br />",

            "test_case_id": "1432349819674",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.123Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 143 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T143",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1124,
        "fields": {
            "title": "算法提高 交换Easy",
            "description": r"<br />　　给定N个整数组成的序列，每次交换当前第x个与第y个整数，要求输出最终的序列。",
            "input_description": r"输入描述:<br />　　第一行为序列的大小N(1&lt;=N&lt;=1000)和操作个数M(1&lt;=M&lt;=1000)。<br /> 　　第二行包含N个数字，表示初始序列。<br /> 　　接下来M行，每行两个整数x,y (1&lt;=x,y&lt;=N)，表示要交换的两个整数。在一次交换中，如果x和y相等，则不会改变序列的内容。 <br />输入样例: <br />5 2<br /> 1 2 3 4 5<br /> 1 2<br /> 3 4",
            "output_description": r"<br />输出描述: <br />　　输出N行，为交换后的序列中的数。<br /> 输出样例: <br />2<br /> 1<br /> 4<br /> 3<br /> 5",

            "test_case_id": "1452388341308",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.125Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 145 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T145",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1126,
        "fields": {
            "title": "算法提高 多项式输出",
            "description": r"<br />　　一元n 次多项式可用如下的表达式表示：<br /> 　　f(x)=a[n]x^n+a[n-1]x^(n-1)+...+a[1]x+a[0], a[n]!=0<br /> 　　其中，a[i]x^i称为i 次项， a[i]称为i 次项的系数。给出一个一元多项式各项的次数和系数，请按照如下规定的格式要求输出该多项式：<br /> 　　1. 多项式中自变量为x，从左到右按照次数递减顺序给出多项式。<br /> 　　2. 多项式中只包含系数不为0 的项。<br /> 　　3. 如果多项式n 次项系数为正，则多项式开头不出现“+”号，如果多项式n 次项系数为负，则多项式以“-”号开头。<br /> 　　4. 对于不是最高次的项，以“+”号或者“-”号连接此项与前一项，分别表示此项系数为正或者系数为负。紧跟一个正整数，表示此项系数的绝对值（如果一个高于0 次的项，其系数的绝对值为1，则无需输出1）。如果x 的指数大于1，则接下来紧跟的指数部分的形式为“x^b”，其中b 为x 的指数；如果x 的指数为1，则接下来紧跟的指数部分形式为“x”；如果x 的指数为0，则仅需输出系数即可。<br /> 　　5. 多项式中，多项式的开头、结尾不含多余的空格。",
            "input_description": r"输入描述:<br />　　输入共有2 行<br /> 　　第一行1 个整数，n，表示一元多项式的次数。<br /> 　　第二行有n+1 个整数，其中第i 个整数表示第n-i+1 次项的系数，每两个整数之间用空格隔开。<br /> 　　1 ≤ n ≤ 100，多项式各次项系数的绝对值均不超过100。 <br />输入样例: <br />5<br /> 100 -1 1 -3 0 10",
            "output_description": r"<br />输出描述: <br />　　输出共1 行，按题目所述格式输出多项式。<br /> 输出样例: <br />100x^5-x^4+x^3-3x^2+10",

            "test_case_id": "1522426862942",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.127Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 152 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T152",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1127,
        "fields": {
            "title": "算法提高 矩阵乘方",
            "description": r"<br />　　给定一个矩阵A,一个非负整数b和一个正整数m，求A的b次方除m的余数。<br /> 　　其中一个nxn的矩阵除m的余数得到的仍是一个nxn的矩阵，这个矩阵的每一个元素是原矩阵对应位置上的数除m的余数。<br /> 　　要计算这个问题，可以将A连乘b次，每次都对m求余，但这种方法特别慢，当b较大时无法使用。下面给出一种较快的算法(用A^b表示A的b次方)：<br /> 　　若b=0，则A^b%m=I%m。其中I表示单位矩阵。<br /> 　　若b为偶数，则A^b%m=(A^(b/2)%m)^2%m，即先把A乘b/2次方对m求余，然后再平方后对m求余。<br /> 　　若b为奇数，则A^b%m=(A^(b-1)%m)*a%m，即先求A乘b-1次方对m求余，然后再乘A后对m求余。<br /> 　　这种方法速度较快，请使用这种方法计算A^b%m，其中A是一个2x2的矩阵，m不大于10000。",
            "input_description": r"输入描述:<br />　　输入第一行包含两个整数b, m，第二行和第三行每行两个整数，为矩阵A。 <br />输入样例: <br />2 2<br /> 1 1<br /> 0 1",
            "output_description": r"<br />输出描述: <br />　　输出两行，每行两个整数，表示A^b%m的值。<br /> 输出样例: <br />1 0<br /> 0 1",

            "test_case_id": "1542446123759",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.128Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 154 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T154",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1128,
        "fields": {
            "title": "算法提高 夺宝奇兵",
            "description": r"<br /><b>[</b><b>题目描述]</b><br /> 　　在一座山上,有很多很多珠宝,它们散落在山底通往山顶的每条道路上,不同道路上的珠宝的数目也各不相同.下图为一张藏宝地图:<br /> <br /> 　　7<br /> 　　3        8<br /> 　　8   1   0<br /> 　　2   7   4   4<br /> 　　4   5   2   6   5<br /> <br /> 　　”夺宝奇兵”从山下出发,到达山顶,如何选路才能得到最多的珠宝呢?在上图所示例子中,按照5-&gt;7-&gt;8-&gt;3-&gt;7的顺序,将得到最大值30<br /> <br /> <b>[</b><b>输入]</b><br /> 　　第一行正整数N(100&gt;=N&gt;1),表示山的高度<br /> 　　接下来有N行非负整数,第i行有i个整数(1&lt;=i&lt;=N),表示山的第i层上从左到右每条路上的珠宝数目<br /> <br /> <b>[</b><b>输出]</b><br /> 　　一个整数,表示从山底到山顶的所能得到的珠宝的最大数目.<br /> <b>[</b><b>样例输入]</b><pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">5</font></span> </pre> <pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">7</font></span> </pre> <pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">3 8</font></span> </pre> <pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">8 1 0 </font></span> </pre> <pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">2 7 4 4</font></span> </pre> <pre class='pddata'> <span lang=\"EN-US\"><font face=\"宋体\" size=\"3\">4 5 2 6 5</font></span> </pre> <br /> <b>[</b><b>样例输出]</b><br /> 　　30",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "1552465384576",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.129Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 155 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T155",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1129,
        "fields": {
            "title": "算法提高 利息计算",
            "description": r"<br />　　编制程序完成下述任务：接受两个数，一个为用户一年期定期存款金额，一个为按照百分比格式表示的利率；程序计算一年期满后本金与利息总额。说明：（1）存款金额以人民币元为单位，可能精确到分；（2）输入利率时不需要输入百分号，例如一年期定期存款年利率为2.52%，用户输入2.52即可；（3）按照国家法律，存款利息所得需缴纳20% 的所得税，计算结果时所得税部分应扣除。",
            "input_description": r"输入描述:<br />　　输入一行，包含两个实数，分别表示本金和年利率。 <br />输入样例: <br />10000  2.52",
            "output_description": r"<br />输出描述: <br />　　输出一行，包含一个实数，保留到小数点后两位，表示一年后的本金与利息和。<br /> 输出样例: <br />10201.60",

            "test_case_id": "1562484645393",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.130Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 156 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T156",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1130,
        "fields": {
            "title": "算法提高 乘法运算",
            "description": r"<br />　　编制一个乘法运算的程序。<br /> 　　从键盘读入2个100以内的正整数，进行乘法运算并以竖式输出。",
            "input_description": r"输入描述:<br />　　输入只有一行，是两个用空格隔开的数字，均在1~99之间（含1和99）。 <br />输入样例: <br />89 13",
            "output_description": r"<br />输出描述: <br />　　输出为4行或7行，符合乘法的竖式运算格式。<br /> 输出样例: <br />89<br /> ×13<br /> ━━━<br /> 267<br /> 89<br /> ━━━<br /> 1157",

            "test_case_id": "1572503906210",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　3×89=267，则第四行267右侧对准个位输出。1×89=89，则第五行89右侧对准十位输出。267+890=1157，则1157右侧对准个位输出。",
            "create_time": "2018-03-28T03:15:44.131Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 157 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T157",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1131,
        "fields": {
            "title": "算法提高 格子位置",
            "description": r"<br />　　输入三个自然数N，i，j （1&lt;=i&lt;=N，1&lt;=j&lt;=N），输出在一个N*N格的棋盘中，与格子（i，j）同行、同列、同一对角线的所有格子的位置。",
            "input_description": r"输入描述:<br />　　输入共三行，分别输入自然数N，i，j。其中保证N&lt;=24且1&lt;=i&lt;=N，1&lt;=j&lt;=N。 <br />输入样例: <br />4<br /> 2<br /> 3",
            "output_description": r"<br />输出描述: <br />　　输出共四行。第一行为与格子（i，j）同行的所有格子的位置，第二行为与格子（i，j）同列的所有格子的位置，第三行为从左上到右下对角线上的格子的位置，第四行为从左下到右上对角线上的格子的位置。<br /> 输出样例: <br />(2,1) (2,2) (2,3) (2,4)<br /> (1,3) (2,3) (3,3) (4,3)<br /> (1,2) (2,3) (3,4)<br /> (4,1) (3,2) (2,3) (1,4)",

            "test_case_id": "1582523167027",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　n=4，i=2，j=3表示了棋盘中的第二行第三列的格子，如下图：<br /> <table cellspacing=0 cellpadding=2px style='border-collapse:collapse;' class='table table-striped table-horver'><tbody><tr  style='border:solid 1.0pt'><td style='border:solid 1.0pt'>第1列</td><td style='border:solid 1.0pt'>第2列</td><td style='border:solid 1.0pt'>第3列</td><td style='border:solid 1.0pt'>第4列</td><td style='border:solid 1.0pt'> </td></tr><tr  style='border:solid 1.0pt'><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'>第1行</td></tr><tr  style='border:solid 1.0pt'><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'>(2,3)</td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'>第2行</td></tr><tr  style='border:solid 1.0pt'><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'>第3行</td></tr><tr  style='border:solid 1.0pt'><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'> </td><td style='border:solid 1.0pt'>第4行</td></tr></tbody></table><br /> 　　(2,1) (2,2) (2,3) (2,4) \t\t\t{同一行上格子的位置}<br /> 　　(1,3) (2,3) (3,3) (4,3)\t\t\t{同列列上格子的位置}<br /> 　　(1,2) (2,3) (3,4)\t         \t{左上到右下对角线上的格子的位置}<br /> 　　(4,1) (3,2) (2,3) (1,4)   \t\t{左下到右上对角线上的格子的位置}",
            "create_time": "2018-03-28T03:15:44.132Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 158 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T158",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1134,
        "fields": {
            "title": "算法提高 阮小二买彩票",
            "description": r"<br />　　在同学们的帮助下，阮小二是变的越来越懒了，连算账都不愿意自己亲自动手了，每天的工作就是坐在电脑前看自己的银行账户的钱是否有变多。可是一段时间观察下来，阮小二发现自己账户的钱增长好慢啊，碰到节假日的时候连个铜板都没进，更郁闷的是这些天分文不进就算了，可恨的是银行这几天还有可能“落井下石”(代扣个人所得税)，看着自己账户的钱被负增长了，阮小二就有被割肉的感觉(太痛苦了！)，这时阮小二最大的愿望无疑是以最快的速度日进斗金，可什么方法能够日进斗金呢？抢银行(老本行)？不行，太危险，怕有命抢没命花；维持现状？受不了，搂钱太慢了！想来想去，抓破脑袋之后，终于想到了能快速发家致富的法宝----买彩票，不但挣了钱有命花，运气好的话，可以每天中他个几百万的，岂不爽哉！抱着这种想法，阮小二开始了他的买彩票之旅。想法是“好的”（太天真了OR 太蠢了），可是又发现自己的数学功底太差，因为不知道数字都有哪些组合排列？那现在就请同学们写个<b>递归</b>程序，帮助阮小二解决一下这个问题吧！",
            "input_description": r"输入描述:<br />　　不超过6位数的正整数N，注意：<b>构成正整数</b><b>N</b><b>的数字可重复</b> <br />输入样例: <br />123",
            "output_description": r"<br />输出描述: <br />　　组成正整数N的所有位数的全排列，这些排列按<b>升序</b>输出，<b>每个排列占一行。</b><br /> <b>   </b><br /> <b>   注意：输出数据中不能有重复的排列</b><br /> 输出样例: <br />123<br /> 132<br /> 213<br /> 231<br /> 312<br /> 321",

            "test_case_id": "1622580949478",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.135Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 162 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T162",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1135,
        "fields": {
            "title": "算法提高 传染病控制",
            "description": r"<br />　　近来，一种新的传染病肆虐全球。蓬莱国也发现了零星感染者，为防止该病在蓬莱国大范围流行，该国政府决定不惜一切代价控制传染病的蔓延。不幸的是，由于人们尚未完全认识这种传染病，难以准确判别病毒携带者，更没有研制出疫苗以保护易感人群。于是，蓬莱国的疾病控制中心决定采取切断传播途径的方法控制疾病传播。经过 WHO（世界卫生组织）以及全球各国科研部门的努力，这种新兴传染病的传播途径和控制方法已经研究消楚，剩下的任务就是由你协助蓬莱国疾控中心制定一个有效的控制办法。",
            "input_description": r"输入描述:<br />　　研究表明，这种传染病的传播具有两种很特殊的性质；<br /> 　　第一是它的传播途径是树型的，一个人X只可能被某个特定的人Y感染，只要Y不得病，或者是XY之间的传播途径被切断，则X就不会得病。<br /> 　　第二是，这种疾病的传播有周期性，在一个疾病传播周期之内，传染病将只会感染一代患者，而不会再传播给下一代。<br /> 　　这些性质大大减轻了蓬莱国疾病防控的压力，并且他们已经得到了国内部分易感人群的潜在传播途径图（一棵树）。但是，麻烦还没有结束。由于蓬莱国疾控中心人手不够，同时也缺乏强大的技术，以致他们在一个疾病传播周期内，只能设法切断一条传播途径，而没有被控制的传播途径就会引起更多的易感人群被感染（也就是与当前已经被感染的人有传播途径相连，且连接途径没有被切断的人群）。当不可能有健康人被感染时，疾病就中止传播。所以，蓬莱国疾控中心要制定出一个切断传播途径的顺序，以使尽量少的人被感染。你的程序要针对给定的树，找出合适的切断顺序。 <br />输入样例: <br />7 6<br /> 1 2<br /> 1 3<br /> 2 4<br /> 2 5<br /> 3 6<br /> 7 3",
            "output_description": r"<br />输出描述: <br />　　输入格式的第一行是两个整数n（1≤n≤300）和p。接下来p行，每一行有两个整数i和j，表示节点i和j间有边相连（意即，第i人和第j人之间有传播途径相连，注意：可能是i到j也可能是j到i）。其中节点1是已经被感染的患者。<br /> 　　对于给定的输入数据，如果不切断任何传播途径，则所有人都会感染。<br /> 输出样例: <br />3",

            "test_case_id": "1632600210295",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　只有一行，输出总共被感染的人数。",
            "create_time": "2018-03-28T03:15:44.136Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 163 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T163",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1136,
        "fields": {
            "title": "算法提高 企业奖金发放",
            "description": r"<br />　　企业发放的奖金根据利润提成。利润低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万元到60万元之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%；高于100万元时，超过100万元的部分按1%提成。从键盘输入当月利润，求应发放奖金总数？（保留两位小数）利润的大小在double以内",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />210000",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />18000.00",

            "test_case_id": "1652619471112",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.137Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 165 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T165",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1137,
        "fields": {
            "title": "算法提高 质因数",
            "description": r"<br />　　将一个正整数N(1&lt;N&lt;32768)分解质因数。例如，输入90，打印出90=2*3*3*5。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />66",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />66=2*3*11",

            "test_case_id": "1662638731929",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.138Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 166 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T166",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1140,
        "fields": {
            "title": "算法提高 一元一次方程",
            "description": r"<br />　　输入一元一次方法的ax+b=0的解。且数据均在double类型以内,且一定有解（保留2位小数）",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />2  6",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />-3.00",

            "test_case_id": "1722696514380",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.141Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 172 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T172",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1141,
        "fields": {
            "title": "算法提高 数组输出",
            "description": r"<br />　　输入一个3行4列的数组，找出该数组中绝对值最大的元素、输出该元素及其两个下标值。如有多个输出行号最小的，还有多个的话输出列号最小的。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />1 2  3  5<br /> -2  5  8  9<br /> 6  -7  5  3",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />9 2 4",

            "test_case_id": "1752715775197",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.142Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 175 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T175",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1142,
        "fields": {
            "title": "算法提高 计算整数因子",
            "description": r"<br />　　输入一个整数，输出其所有质因子。",
            "input_description": r"输入描述:<br />　　输入只有一行，包含一个整数n。 <br />输入样例: <br />6",
            "output_description": r"<br />输出描述: <br />　　输出一行，包含若干个整数，为n的所有质因子，按照从小到大的顺序排列。<br /> 输出样例: <br />2 3",

            "test_case_id": "1762735036014",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　1&lt;=n&lt;=10000。",
            "create_time": "2018-03-28T03:15:44.143Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 176 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T176",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1143,
        "fields": {
            "title": "算法提高 最长单词",
            "description": r"<br />　　编写一个函数，输入一行字符，将此字符串中最长的单词输出。<br /> 　　输入仅一行，多个单词，每个单词间用一个空格隔开。单词仅由小写字母组成。所有单词的长度和不超过100000。如有多个最长单词，输出最先出现的。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />I am a student",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />student",

            "test_case_id": "1812754296831",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.144Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 181 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T181",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1145,
        "fields": {
            "title": "算法提高 时间转换",
            "description": r"<br />　　输入n分钟换算成天、小时和分输出。例如4880分钟，可换算成3天9小时20分。<br /> 　　输入一个正整数n(1",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />4880",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />3  9  20",

            "test_case_id": "1832792818465",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.146Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 183 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T183",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1147,
        "fields": {
            "title": "算法提高 寻找三位数",
            "description": r"<br />　　将1，2，…，9共9个数分成三组，分别组成三个三位数，且使这三个三位数构成<br /> 　　1：2：3的比例，试求出所有满足条件的三个三位数。<br /> 　　例如：三个三位数192，384，576满足以上条件。",
            "input_description": r"输入描述:<br />　　无输入文件 <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　输出每行有三个数，为满足题设三位数。各行为满足要求的不同解。<br /> 输出样例: <br />",

            "test_case_id": "1892831340099",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.148Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 189 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T189",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1148,
        "fields": {
            "title": "算法提高 图形输出",
            "description": r"<br />　　编写一程序，在屏幕上输出如下内容：<br /> 　　X | X | X<br /> 　　---+---+---<br /> 　　|   |<br /> 　　---+---+---<br /> 　　O | O | O<br /> 　　注意：本题请同学们严格按照图形的格式输出，对齐，其中X和O为大写，否则系统会判为错误。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "1902850600916",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.149Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 190 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T190",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1149,
        "fields": {
            "title": "算法提高 利息计算",
            "description": r"<br />　　编制程序完成下述任务：接受两个数，一个为用户一年期定期存款金额，一个为按照百分比格式表示的利率；程序计算一年期满<br /> 　　后本金与利息总额。说明：（1）存款金额以人民币元为单位，可能精确到分；（2）输入利率时不需要输入百分号，例如一年期定期存款年利率<br /> 　　为2.52%，用户输入2.52即可；（3）按照国家法律，存款利息所得需缴纳20% 的所得税，计算结果时所得税部分应扣除。要求输出小数点后严格<br /> 　　保留两位小数。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />10000   2.52",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />10201.60",

            "test_case_id": "1932869861733",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.150Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 193 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T193",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1150,
        "fields": {
            "title": "算法提高 输出九九乘法表",
            "description": r"<br />　　注意：表头的大小写要和样例一致，短线“-”个数要与样例中一致，否则系统会判为错误。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "1952889122550",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.151Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 195 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T195",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1151,
        "fields": {
            "title": "算法提高 任意年月日历输出",
            "description": r"<br />",
            "input_description": r"输入描述:<br /> <br />输入样例: <br /><pre class='pddata'> 已知2007年1月1日为星期一。 设计一函数按照下述格式打印2007年以后（含）某年某月的日历，2007年以前的拒绝打印。 为完成此函数，设计必要的辅助函数可能也是必要的。其中输入为年分和月份。 </pre>",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "1992908383367",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.152Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 199 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T199",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1154,
        "fields": {
            "title": "算法提高 字符串比较",
            "description": r"<br />",
            "input_description": r"输入描述:<br /> <br />输入样例: <br /><pre class='pddata'> 独立实现标准字符串库的strcmp函数，即字符串比较函数，从键盘输入两个字符串，按字典序比较大小，前者大于后者输出1，前者小于后者输出-1，两者相等输出0。 </pre>",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2042966165818",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.155Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 204 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T204",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1155,
        "fields": {
            "title": "算法提高 复数求和",
            "description": r"<br />",
            "input_description": r"输入描述:<br /> <br />输入样例: <br /><pre class='pddata'> 从键盘读入n个复数（实部和虚部都为整数）用链表存储，遍历链表求出n个复数的和并输出。 样例输入: <br />3 <br />3 4<br />5 2<br />1 3<br />样例输出:<br />9+9i </pre>",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2062985426635",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.156Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 206 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T206",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1157,
        "fields": {
            "title": "算法提高 栅格打印问题",
            "description": r"<br />　　编写一个程序，输入两个整数，作为栅格的高度和宽度，然后用“+”、“-”和“|”这三个字符来打印一个栅格。<br /> 　　输入格式：输入只有一行，包括两个整数，分别为栅格的高度和宽度。<br /> 　　输出格式：输出相应的栅格。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />3 2",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />+-+-+<br /> | | |<br /> +-+-+<br /> | | |<br /> +-+-+<br /> | | |<br /> +-+-+",

            "test_case_id": "2103023948269",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.158Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 210 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T210",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1158,
        "fields": {
            "title": "算法提高 断案",
            "description": r"<br />　　公安人员审问甲、乙、丙、丁四个嫌疑犯，已确知，这四个人当中仅有一人是偷窃者，还知道这四个人的答话，要么完全诚实，要么完全说谎。在回答公安人员的问话中：<br /> 　　甲说：“乙没有偷，是丁偷的。”<br /> 　　乙说：“我没有偷，是丙偷的。”<br /> 　　丙说：“甲没有偷，是乙偷的。”<br /> 　　丁说：“我没有偷，我用的那东西是我家里的。”<br /> 　　请根据上述四人答话，判断谁是偷窃者。<br /> 　　输入格式：无输入。<br /> 　　输出格式：输出一个字符，表示偷窃者是谁，A表示甲，B表示乙，C表示丙，D表示丁。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2123043209086",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.159Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 212 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T212",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1160,
        "fields": {
            "title": "算法提高 单词个数统计",
            "description": r"<br />　　编写一个程序，输入一个字符串（长度不超过80），然后统计出该字符串当中包含有多少个单词。例如：字符串“this is a book”当中包含有4个单词。<br /> 　　输入格式：输入一个字符串，由若干个单词组成，单词之间用一个空格隔开。<br /> 　　输出格式：输出一个整数，即单词的个数。<br /> 　　输入输出样例<br /> 　　用户输入数据样例：<br /> 　　this is a book<br /> 　　系统输出数据如下：<br /> 　　4",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2143081730720",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.161Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 214 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T214",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1166,
        "fields": {
            "title": "算法提高 打水问题",
            "description": r"<br />　　N个人要打水，有M个水龙头，第i个人打水所需时间为Ti，请安排一个合理的方案使得所有人的等待时间之和尽量小。",
            "input_description": r"输入描述:<br />　　第一行两个正整数N M 接下来一行N个正整数Ti。<br /> 　　N,M&lt;=1000，Ti&lt;=1000 <br />输入样例: <br />7 3<br /> 3 6 1 4 2 5 7",
            "output_description": r"<br />输出描述: <br />　　最小的等待时间之和。（不需要输出具体的安排方案）<br /> 输出样例: <br />11",

            "test_case_id": "2243197295622",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　一种最佳打水方案是，将N个人按照Ti从小到大的顺序依次分配到M个龙头打水。<br /> 　　例如样例中，Ti从小到大排序为1，2，3，4，5，6，7，将他们依次分配到3个龙头，则去龙头一打水的为1，4，7；去龙头二打水的为2,5；去第三个龙头打水的为3,6。<br /> 　　第一个龙头打水的人总等待时间 = 0 + 1 + (1 + 4) = 6<br /> 　　第二个龙头打水的人总等待时间 = 0 + 2 = 2<br /> 　　第三个龙头打水的人总等待时间 = 0 + 3 = 3<br /> 　　所以总的等待时间 = 6 + 2 + 3 = 11",
            "create_time": "2018-03-28T03:15:44.167Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 224 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T224",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1169,
        "fields": {
            "title": "算法提高 不同单词个数统计",
            "description": r"<br /><b> </b><br /> <b>问题描述</b><br /> 　　编写一个程序，输入一个句子，然后统计出这个句子当中不同的单词个数。例如：对于句子“one little two little three little boys”，总共有5个不同的单词：one, little, two, three, boys。<br /> 　　说明：（1）由于句子当中包含有空格，所以应该用gets函数来输入这个句子；（2）输入的句子当中只包含英文字符和空格，单词之间用一个空格隔开；（3）不用考虑单词的大小写，假设输入的都是小写字符；（4）句子长度不超过100个字符。<br /> 　　输入格式：输入只有一行，即一个英文句子。<br /> 　　输出格式：输出只有一行，是一个整数，表示句子中不同单词的个数。<br /> <b>输入输出样例</b>",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />one little two little three little boys",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />5<br /> <b> </b>",

            "test_case_id": "2283255078073",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.170Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 228 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T228",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1170,
        "fields": {
            "title": "算法提高 欧拉函数",
            "description": r"<br />　　2016.4.5 已更新试题，请重新提交自己的程序。",
            "input_description": r"输入描述:<br />　　给定一个大于1，不超过2000000的正整数n，输出欧拉函数，phi(n)的值。<br /> 　　如果你并不了解欧拉函数，那么请参阅提示。 <br />输入样例: <br />17",
            "output_description": r"<br />输出描述: <br />　　在给定的输入文件中进行读入：<br /> 　　一行一个正整数n。<br /> 输出样例: <br />16",

            "test_case_id": "2293274338890",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　将输出信息输出到指定的文件中:<br /> 　　一行一个整数表示phi(n)。",
            "create_time": "2018-03-28T03:15:44.171Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 229 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T229",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1171,
        "fields": {
            "title": "算法提高 分数统计",
            "description": r"<br />　　2016.4.5已更新此题，此前的程序需要重新提交。",
            "input_description": r"输入描述:<br />　　给定一个百分制成绩T，将其划分为如下五个等级之一：<br /> 　　90~100为A，80~89为B，70~79为C，60~69为D，0~59为E<br /> 　　现在给定一个文件inp，文件中包含若干百分制成绩（成绩个数不超过100），请你统计五个等级段的人数，并找出人数最多的那个等级段，按照从大到小的顺序输出该段中所有人成绩（保证人数最多的等级只有一个）。要求输出到指定文件oup中。 <br />输入样例: <br />100 80 85 77 55 61 82 90 71 60",
            "output_description": r"<br />输出描述: <br />　　若干0~100的正整数，用空格隔开<br /> 输出样例: <br />2 3 2 2 1<br /> 3<br /> 85 82 80",

            "test_case_id": "2313293599707",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />　　第一行为5个正整数，分别表示A,B,C,D,E五个等级段的人数<br /> 　　第二行一个正整数，表示人数最多的等级段中人数<br /> 　　接下来一行若干个用空格隔开的正整数，表示人数最多的那个等级中所有人的分数，按从大到小的顺序输出。",
            "create_time": "2018-03-28T03:15:44.172Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 231 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T231",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1172,
        "fields": {
            "title": "算法提高 Quadratic Equation",
            "description": r"<br />　　求解方程ax<sup>2</sup>+bx+c=0的根。要求a, b, c由用户输入，并且可以为任意实数。<br /> 　　输入格式：输入只有一行，包括三个系数，之间用空格格开。<br /> 　　输出格式：输出只有一行，包括两个根，大根在前，小根在后，无需考虑特殊情况，保留小数点后两位。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />2.5 7.5 1.0",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />-0.14 -2.86",

            "test_case_id": "2343312860524",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.173Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 234 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T234",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1173,
        "fields": {
            "title": "算法提高 c++_ch02_02",
            "description": r"<br />　　使用Switch语句编写一个模拟简单计算器的程序。依次输入两个整数和一个字符，并用空格隔开。如果该字符是一个“+”，则打印和；如果该字符是一个“-”，则打印差；如果该字符是一个“*”,则打印积；如果该字符是“/”，则打印商；如果该字符是一个“%”，则打印余数。打印结果后输出一个空行。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2383332121341",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.174Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 238 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T238",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1174,
        "fields": {
            "title": "算法提高 c++_ch02_03",
            "description": r"<br />　　编写程序实现“剪刀，石头，布”游戏。在这个游戏中，两个人同时说“剪刀”，“石头”或“布”，压过另一方的为胜者。规则是：“布”胜过“石头”，“石头”胜过“剪刀”，“剪刀”胜过“布”。要求：选择结构中使用枚举类型，结果的输出也使用枚举类型表示。<br /> 　　输入：两个数，范围为{0,1,2}，用空格隔开。0表示石头，1表示布，2表示剪刀。这两个数分别表示两个人所说的物品。<br /> 　　输出：如果前者赢，输出1。如果后者赢，输出-1。如果是平局，输出0。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2393351382158",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.175Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 239 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T239",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1175,
        "fields": {
            "title": "算法提高 c++_ch03_02",
            "description": r"<br />　　PASCAL三角是形状如下的三角矩阵：<br /> 　　1<br /> 　　1 1<br /> 　　1 2 1<br /> 　　1 3 3 1<br /> 　　1 4 6 4 1<br /> 　　在PASCAL三角中的每个数是一个组合C(n,k)。<br /> 　　C(n,k)=(((((((n/1)(n-1))/2(n-2))/3)***(n-k+2))/(k-1))(n-k+1))/k<br /> 　　公式中交替使用乘法和除法，每次将从n开始递减的一个值相乘，然后除以下一个从1开始递增的值。<br /> 　　如果对行和列从0开始计数，则数字C(n,k)在n行k列。例如C(6,2)在第6行第2列。编程输出指定阶数的PASCAL三角矩阵。例如下面给出的是12阶PASCAL三角形矩阵。<br /> <br /> 　　编写程序，使运行结果为：<br /> 　　1<br /> 　　1   1<br /> 　　1   2   1<br /> 　　1   3   3   1<br /> 　　1   4   6   4   1<br /> 　　1   5  10  10   5   1<br /> 　　1   6  15  20  15   6   1<br /> 　　1   7  21  35  35  21   7   1<br /> 　　1   8  28  56  70  56  28   8   1<br /> 　　1   9  36  84 126 126  84  36   9   1<br /> 　　1  10  45 120 210 252 210 120  45  10   1<br /> 　　1  11  55 165 330 462 462 330 165  55  11   1<br /> 　　1  12  66 220 495 792 924 792 495 220  66  12   1<br /> <br /> <br /> 　　该题的详细文档及程序框架请从网络学堂下载！",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2403370642975",
            "hint": r"HINT:时间限制：3.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.176Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 240 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T240",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1177,
        "fields": {
            "title": "算法提高 进制转换",
            "description": r"<br />　　程序提示用户输入三个字符，每个字符取值范围是0-9，A-F。然后程序会把这三个字符转化为相应的十六进制整数，并分别以十六进制，十进制，八进制输出。<br /> 　　输入格式：输入只有一行，即三个字符。<br /> 　　输出格式：输出只有一行，包括三个整数，中间用空格隔开。<br /> 　　输入输出样例",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />FFF",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />FFF 4095 7777",

            "test_case_id": "2423409164609",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.178Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 242 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T242",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1183,
        "fields": {
            "title": "算法提高 3-2字符串输入输出函数",
            "description": r"<br />　　编写函数GetReal和GetString，在main函数中分别调用这两个函数。在读入一个实数和一个字符串后，将读入的结果依次用printf输出。<br /> 　　两次输入前要输出的提示信息分别是\"please input a number:\\n”和\"please input a string:\\n\"",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />9.56<br /> hello",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />please input a number:<br /> please input a string:<br /> 9.56<br /> hello",

            "test_case_id": "2503524729511",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.184Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 250 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T250",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1187,
        "fields": {
            "title": "算法提高 6-9删除数组中的0元素",
            "description": r"<br />　　编写函数CompactIntegers，删除数组中所有值为0的元素，其后元素向数组首端移动。注意，CompactIntegers函数需要接收数组及其元素个数作为参数，函数返回值应为删除操作执行后数组的新元素个数。<br /> 　　输入时首先读入数组长度，再依次读入每个元素。<br /> 　　将调用此函数后得到的数组和函数返回值输出。",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />7<br /> 2 0 4 3 0 0 5",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />2 4 3 5<br /> 4",

            "test_case_id": "2543601772779",
            "hint": r"HINT:时间限制：1.0s  内存限制：512.0MB<br />",
            "create_time": "2018-03-28T03:15:44.188Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 254 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T254",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1189,
        "fields": {
            "title": "算法提高 高精度加法",
            "description": r"<br />　　在C/C++语言中，整型所能表示的范围一般为-2<sup>31</sup>到2<sup>31</sup>（大约21亿）,即使long long型，一般也只能表示到-2<sup>63</sup>到2<sup>63</sup>。要想计算更加规模的数，就要用软件来扩展了，比如用数组或字符串来模拟更多规模的数及共运算。<br /> 　　现在输入两个整数，请输出它们的和。",
            "input_description": r"输入描述:<br />　　两行，每行一个整数，每个整数不超过1000位 <br />输入样例: <br />15464315464465465<br /> 482321654151",
            "output_description": r"<br />输出描述: <br />　　一行，两个整数的和。<br /> 输出样例: <br />15464797786119616",

            "test_case_id": "2573640294413",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　每个整数不超过1000位",
            "create_time": "2018-03-28T03:15:44.190Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 257 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T257",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1190,
        "fields": {
            "title": "算法提高 去注释",
            "description": r"<br />　　<br /> 　　去注释",
            "input_description": r"输入描述:<br />　　给你一段C++代码，将其中的注释去除后输出剩余的代码。<br /> 　　注释共有两种形式：<br /> 　　1.       行注视：以//开头，一直作用到行尾为止。<br /> 　　例子：<br /> 　　int n;<b>//n</b><b>表示数据规模</b><br /> 　　int a;<br /> 　　去注释后：<br /> 　　int n;<br /> 　　int a;<br /> 　　注意：保留行尾换行符<br /> 　　2.       段注视：以/*开头，到*//结尾，中间部分都是注释，可以跨行。<br /> 　　例子：<br /> 　　int main() {<br /> 　　/*<br /> 　　我是<br /> 　　一段<br /> 　　注释<br /> 　　*/<br /> 　　}<br /> 　　去注释后：<br /> 　　int main() {<br /> <br /> 　　}<br /> 　　注意：由于在线评测系统（Online Judge）对网页显示文本作了格式化，一些空行会被删去，导致上面显示的删除后的结果不正确。删除注释后，剩余的代码应该是三行，两行代码之间有一个空行。这是因为：在段注释结尾符的后面有一个换行符，它不在注释内，需要保留。 <br />输入样例: <br />int main() {<br /> /*<br /> 我是<br /> 一段<br /> 注释<br /> */<br /> int n;//n表示数据规模<br /> }",
            "output_description": r"<br />输出描述: <br />　　一段C++程序代码<br /> 输出样例: <br />int main() {<br /> <br /> int n;<br /> }<br /> <br /> 注意：和之前题目中的解释一样，在int n;之前有一个空行，被在线评测系统删掉，实际程序输出应该有该空行。",

            "test_case_id": "2583659555230",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　去掉注释部分后的程序",
            "create_time": "2018-03-28T03:15:44.191Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 258 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T258",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1191,
        "fields": {
            "title": "算法提高 凶手",
            "description": r"<br />　　巴斯维克命案抓住了六个嫌疑犯，他们的口供如下：<br /> 　　A：我不是罪犯<br /> 　　B：A、C中有一个是罪犯<br /> 　　C：A和B说了假话<br /> 　　D：C和F说了假话<br /> 　　E：其他五个人中，只有A和D说了真话<br /> 　　F：我是罪犯<br /> 　　他们中只有一半说了真话，凶手只有一个。<br /> 　　本题可能有多种可能性，即正确答案（找到唯一的凶手）可能有多个，但每一个可能的答案（某一个是凶手）都满足上述口供。<br /> 　　请编程找出可能的凶手输出。<br /> 　　样例：（假设唯一的凶手是A或者D或者E，则输出结果为三行，按字母顺序依次输出）<br /> 　　A<br /> 　　D<br /> 　　E",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2603678816047",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.192Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 260 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T260",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1193,
        "fields": {
            "title": "算法提高 促销购物",
            "description": r"<br />　　张超来到了超市购物。<br /> 　　每个物品都有价格，正好赶上商店推出促销方案。就是把许多东西一起买更便宜（保证优惠方案一定比原价便宜）。物品要买正好的个数，而且不能为了便宜而买不需要的物品。<br /> 　　张超拿到了优惠方案，和需要购买的物品清单，当然想求出最小的花费。他是信息学选手，自然地想到写个程序解决问题。",
            "input_description": r"输入描述:<br />　　第一行促销物品的种类数（0 &lt;= s &lt;= 99）。<br /> 　　第二行..第s+1 行每一行都用几个整数来表示一种促销方式。<br /> 　　第一个整数 n （1 &lt;= n &lt;= 5），表示这种优惠方式由 n 种商品组成。<br /> 　　后面 n 对整数 c 和 k 表示 k （1 &lt;= k &lt;= 5）个编号为 c （1 &lt;= c &lt;= 999）的商品共同构成这种方案。<br /> 　　最后的整数 p 表示这种优惠的优惠价（1 &lt;= p &lt;= 9999）。也就是把当前的方案中的物品全买需要的价格。<br /> 　　第 s+2 行这行一个整数b （0 &lt;= b &lt;= 5），表示需要购买 b 种不同的商品。<br /> 　　第 s+3 行..第 s+b+2 行这 b 行中的每一行包括三个整数：c ，k ，和 p 。<br /> 　　C 表示唯一的商品编号（1 &lt;= c &lt;= 999），<br /> 　　k 表示需要购买的 c 商品的数量（1 &lt;= k &lt;= 5）。<br /> 　　p 表示 c 商品的原价（1 &lt;= p &lt;= 999）。<br /> 　　最多购买 5*5=25 个商品。 <br />输入样例: <br />2<br /> 1 7 3 5<br /> 2 7 1 8 2 10<br /> 2<br /> 7 3 2<br /> 8 2 5",
            "output_description": r"<br />输出描述: <br />　　一个整数ans，表示需要花的最小费用<br /> 输出样例: <br />14",

            "test_case_id": "2623717337681",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.194Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 262 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T262",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1195,
        "fields": {
            "title": "算法提高 扫雷",
            "description": r"<br />　　扫雷游戏你一定玩过吧！现在给你若干个n×m的地雷阵，请你计算出每个矩阵中每个单元格相邻单元格内地雷的个数，每个单元格最多有8个相邻的单元格。 0&lt;n,m&lt;=100",
            "input_description": r"输入描述:<br />　　输入包含若干个矩阵，对于每个矩阵，第一行包含两个整数n和m，分别表示这个矩阵的行数和列数。接下来n行每行包含m个字符。安全区域用‘.’表示，有地雷区域用'*'表示。当n=m=0时输入结束。 <br />输入样例: <br />4 4<br /> *...<br /> ....<br /> .*..<br /> ....<br /> 3 5<br /> **...<br /> .....<br /> .*...<br /> 0 0",
            "output_description": r"<br />输出描述: <br />　　对于第i个矩阵，首先在单独的一行里打印序号：“Field #i:”,接下来的n行中，读入的'.'应被该位置周围的地雷数所代替。输出的每两个矩阵必须用一个空行隔开。<br /> 输出样例: <br />Field #1:<br /> *100<br /> 2210<br /> 1*10<br /> 1110<br /> <br /> Field #2:<br /> **100<br /> 33200<br /> 1*100<br /> （注意两个矩阵之间应该有一个空行，由于oj的格式化这里不能显示出来）",

            "test_case_id": "2643755859315",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　0&lt;n,m&lt;=100",
            "create_time": "2018-03-28T03:15:44.196Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 264 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T264",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1197,
        "fields": {
            "title": "算法提高 找素数",
            "description": r"<br />　　给定区间[L, R]  ， 请计算区间中素数的个数。",
            "input_description": r"输入描述:<br />　　两个数L和R。 <br />输入样例: <br />2 11",
            "output_description": r"<br />输出描述: <br />　　一行，区间中素数的个数。<br /> 输出样例: <br />5",

            "test_case_id": "2673794380949",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　2 &lt;=  L &lt;= R &lt;= 2147483647        R-L &lt;= 1000000",
            "create_time": "2018-03-28T03:15:44.198Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 267 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T267",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1198,
        "fields": {
            "title": "算法提高 插入排序",
            "description": r"<br />　　<br /> 　　插入排序",
            "input_description": r"输入描述:<br />　　排序，顾名思义，是将若干个元素按其大小关系排出一个顺序。形式化描述如下：有n个元素a[1]，a[2]，…，a[n]，从小到大排序就是将它们排成一个新顺序a[i[1]]&lt;a[i[2]]&lt;…&lt;a[i[n]]<br /> 　　i[k]为这个新顺序。<br /> 　　插入排序，顾名思义，是通过插入操作完成排序。其直觉和方法来源于打牌时安排牌的方法。每次摸起一张牌，你都会将其插入到现在手牌中它按顺序应在的那个位置。插入排序每一步都类似这个摸牌过程。比如现在有整数数组：{3, 1, 5, 4, 2}<br /> 　　第一步：插入3 得到新序列{3}<br /> 　　第二步：插入1 得到新序列{1 3}<br /> 　　第三步：插入5 得到新序列{1 3 5}<br /> 　　第四步：插入4 得到新序列{1 3 4 5}<br /> 　　第五步：插入2 得到新序列{1 2 3 4 5}<br /> 　　为了看程序中如何完成插入过程，我们以第五步为例：<br /> 　　初始时：1 3 4 5 2<br /> 　　将2存入临时变量tmp<br /> 　　将下标j指向2之前的元素5，然后根据tmp和a[j]的大小关系决定该元素是否应该后移。如果a[j]&gt;tmp，则将a[j]后移到a[j+1]，序列变成1 3 4 5 5。<br /> 　　将下标j前移<br /> 　　判断a[j]&gt;tmp，后移a[j]到a[j+1]，得到1 3 4 4 5<br /> 　　将下标j前移<br /> 　　判断a[j]&gt;tmp，后移a[j]到a[j+1]，得到1 3 3 4 5<br /> 　　因为a[j]&lt;=tmp，所以将tmp放回a[j+1]，得到 1 2 3 4 5<br /> 　　现在，输入n个整数，根据以上算法，输出插入排序的全过程。 <br />输入样例: <br />5<br /> 3 1 5 4 2",
            "output_description": r"<br />输出描述: <br />　　第一行一个正整数n，表示元素个数<br /> 　　第二行为n个整数，以空格隔开<br /> 输出样例: <br />Insert element[1]:<br /> Init:3<br /> Final:3<br /> Insert element[2]:<br /> Init:3 1<br /> Move back:3 3<br /> Final:1 3<br /> Insert element[3]:<br /> Init:1 3 5<br /> Final:1 3 5<br /> Insert element[4]:<br /> Init:1 3 5 4<br /> Move back:1 3 5 5<br /> Final:1 3 4 5<br /> Insert element[5]:<br /> Init:1 3 4 5 2<br /> Move back:1 3 4 5 5<br /> Move back:1 3 4 4 5<br /> Move back:1 3 3 4 5<br /> Final:1 2 3 4 5",

            "test_case_id": "2683813641766",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　有n个元素，因此输出部分分为n个部分，每个部分开头行为：Insert element[i]，i为第几个元素。然后对于每一个部分，输出该部分该元素在插入排序过程中的每一步产生的新序列，初始时的序列以Init:打头，然后每一步后移数组元素后的元素序列以Move back:打头，最后得到的最终结果序列以Final:打头。序列元素间以一个空格隔开。示例请看样例输出。每一个部分的Insert element[i]之后的每一步的输出行之前要缩进两格，即输出两个空格。",
            "create_time": "2018-03-28T03:15:44.199Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 268 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T268",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1199,
        "fields": {
            "title": "算法提高 色盲的民主",
            "description": r"<br />　　<br /> 　　色盲的民主",
            "input_description": r"输入描述:<br />　　n个色盲聚在一起，讨论一块布的颜色。尽管都是色盲，却盲得各不相同。每个人都有自己的主张，争论不休。最终，他们决定采取民主投票的方式决定布的颜色，不管布同不同意。某种颜色用字符串表示(字符串为颜色单词或词组，也就是可能有被空格隔开的两个单词组成的颜色词组)，只要字符串不同，程序即判断颜色不同。现在给出这n个人所选择的颜色，输出最有可能的颜色（也就是获得投票最多的颜色），如果有多个颜色获得了最多的投票，则将它们按字典序分行全部输出。 <br />输入样例: <br />5<br /> red<br /> blue<br /> black<br /> black<br /> blue",
            "output_description": r"<br />输出描述: <br />　　第一行一个正整数n，表示色盲的人数<br /> 　　接下来n行，每行一句话<br /> 输出样例: <br />black<br /> blue",

            "test_case_id": "2693832902583",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　若干行，获得投票最多的颜色，按字典序输出",
            "create_time": "2018-03-28T03:15:44.200Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 269 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T269",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1200,
        "fields": {
            "title": "算法提高 选择排序",
            "description": r"<br />　　<br /> 　　选择排序",
            "input_description": r"输入描述:<br />　　排序，顾名思义，是将若干个元素按其大小关系排出一个顺序。形式化描述如下：有n个元素a[1]，a[2]，…，a[n]，从小到大排序就是将它们排成一个新顺序a[i[1]]&lt;a[i[2]]&lt;…&lt;a[i[n]]<br /> 　　i[k]为这个新顺序。<br /> 　　选择排序的思想极其简单，每一步都把一个最小元素放到前面，如果有多个相等的最小元素，选择排位较考前的放到当前头部。还是那个例子：{3 1 5 4 2}：<br /> 　　第一步将1放到开头（第一个位置），也就是交换3和1，即swap(a[0],a[1])得到{1 3 5 4 2}<br /> 　　第二步将2放到第二个位置，也就是交换3和2，即swap(a[1],a[4])得到{1 2 5 4 3}<br /> 　　第三步将3放到第三个位置，也就是交换5和3，即swap(a[2],a[4])得到{1 2 3 4 5}<br /> 　　第四步将4放到第四个位置，也就是交换4和4，即swap(a[3],a[3])得到{1 2 3 4 5}<br /> 　　第五步将5放到第五个位置，也就是交换5和5，即swap(a[4],a[4])得到{1 2 3 4 5}<br /> 　　输入n个整数，输出选择排序的全过程。<br /> 　　要求使用递归实现。 <br />输入样例: <br />5<br /> 4 3 1 1 2",
            "output_description": r"<br />输出描述: <br />　　第一行一个正整数n，表示元素个数<br /> 　　第二行为n个整数，以空格隔开<br /> 输出样例: <br />swap(a[0], a[2]):1 3 4 1 2<br /> swap(a[1], a[3]):1 1 4 3 2<br /> swap(a[2], a[4]):1 1 2 3 4<br /> swap(a[3], a[3]):1 1 2 3 4<br /> swap(a[4], a[4]):1 1 2 3 4",

            "test_case_id": "2703852163400",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　共n行，每行输出第n步选择时交换哪两个位置的下标，以及交换得到的序列，格式:<br /> 　　swap(a[i],a[j]):a[0] … a[n-1]<br /> 　　i和j为所交换元素的下标，下标从0开始，最初元素顺序按输入顺序。另外请保证i&lt;=j<br /> 　　a[0]…a[n-1]为交换后的序列，元素间以一个空格隔开",
            "create_time": "2018-03-28T03:15:44.201Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 270 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T270",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1202,
        "fields": {
            "title": "算法提高 笨小猴",
            "description": r"<br />　　笨小猴的词汇量很小，所以每次做英语选择题的时候都很头疼。但是他找到了一种方法，经试验证明，用这种方法去选择选项的时候选对的几率非常大！<br /> 　　这种方法的具体描述如下：假设maxn是单词中出现次数最多的字母的出现次数，minn是单词中出现次数最少的字母的出现次数，如果maxn-minn是一个质数，那么笨小猴就认为这是个Lucky Word，这样的单词很可能就是正确的答案。",
            "input_description": r"输入描述:<br />　　输入文件只有一行，是一个单词，其中只可能出现小写字母，并且长度小于100。 <br />输入样例: <br />error",
            "output_description": r"<br />输出描述: <br />　　输出文件共两行，第一行是一个字符串，假设输入的的单词是Lucky Word，那么输出“Lucky Word”，否则输出“No Answer”；第二行是一个整数，如果输入单词是Lucky Word，输出maxn-minn的值，否则输出0。<br /> 输出样例: <br />Lucky Word<br /> 2",

            "test_case_id": "2723890685034",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　单词error中出现最多的字母r出现了3次，出现次数最少的字母出现了1次，3-1=2，2是质数。",
            "create_time": "2018-03-28T03:15:44.203Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 272 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T272",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1203,
        "fields": {
            "title": "算法提高 彩票",
            "description": r"<br />　　为丰富男生节活动，贵系女生设置彩票抽奖环节，规则如下：<br /> 　　1、每张彩票上印有7个各不相同的号码，且这些号码的取值范围为[1, 33]；<br /> 　　2、每次在兑奖前都会公布一个由七个互不相同的号码构成的中奖号码；<br /> 　　3、共设置7个奖项，特等奖和一等奖至六等奖。兑奖规则如下：<br /> 　　特等奖：要求彩票上的7个号码都出现在中奖号码中；<br /> 　　一等奖：要求彩票上的6个号码出现在中奖号码中；<br /> 　　二等奖：要求彩票上的5个号码出现在中奖号码中；<br /> 　　……<br /> 　　六等奖：要求彩票上的1个号码出现在中奖号码中；<br /> 　　注：不考虑号码出现的顺序，例如若中奖号码为23 31 1 14 19 17 18，则彩票12 8 9 23 1 16 7由于其中有两个号码（23和1）出现在中奖号码中，所以该彩票中了五等奖。<br /> 　　现已知中奖号码和李华买的若干彩票的号码，请你写一个程序判断他的彩票中奖情况。",
            "input_description": r"输入描述:<br />　　第一行一个正整数n，表示彩票数量，第二行7个整数，表示中奖号码，下面n行每行7个整数，描述n张彩票。 <br />输入样例: <br />3<br /> 1 2 3 4 5 6 7<br /> 11 12 13 14 15 16 17<br /> 12 13 14 15 16 17 18<br /> 8 7 10 9 31 30 29",
            "output_description": r"<br />输出描述: <br />　　7个空格隔开的数字，第1个数字表示特等奖的中奖张数，第2个数字表示一等奖的中奖张数，第3个数字表示二等奖的中奖张数……第7个数字表示六等奖的中奖张数。<br /> 输出样例: <br />0 0 0 0 0 0 1",

            "test_case_id": "2733909945851",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　30%的数据n&lt;=100；<br /> 　　70%的数据n&lt;=1000；<br /> 　　100%的数据n&lt;=100000。<br /> <br /> 　　*****提示：数组定义为全局变量，可以分配更多内存。*****",
            "create_time": "2018-03-28T03:15:44.204Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 273 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T273",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1204,
        "fields": {
            "title": "算法提高 校门外的树",
            "description": r"<br />　　某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；数轴上的每个整数点，即0，1，2，……，L，都种有一棵树。<br /> 　　由于马路上有一些区域要用来建地铁。这些区域用它们在数轴上的起始点和终止点表示。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，马路上还有多少棵树。",
            "input_description": r"输入描述:<br />　　输入的第一行有两个整数L（1 &lt;= L &lt;= 10000）和 M（1 &lt;= M &lt;= 100），L代表马路的长度，M代表区域的数目，L和M之间用一个空格隔开。接下来的M行每行包含两个不同的整数，用一个空格隔开，表示一个区域的起始点和终止点的坐标。 <br />输入样例: <br />500 3<br /> 150 300<br /> 100 200<br /> 470 471",
            "output_description": r"<br />输出描述: <br />　　输出包括一行，这一行只包含一个整数，表示马路上剩余的树的数目。<br /> 输出样例: <br />298",

            "test_case_id": "2743929206668",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于20%的数据，区域之间没有重合的部分；<br /> 　　对于其它的数据，区域之间有重合的情况。",
            "create_time": "2018-03-28T03:15:44.205Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 274 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T274",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1206,
        "fields": {
            "title": "算法提高 大数加法",
            "description": r"<br />　　输入两个正整数a,b，输出a+b的值。",
            "input_description": r"输入描述:<br />　　两行，第一行a，第二行b。a和b的长度均小于1000位。 <br />输入样例: <br />4<br /> 2",
            "output_description": r"<br />输出描述: <br />　　一行，a+b的值。<br /> 输出样例: <br />6",

            "test_case_id": "2773967728302",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.207Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 277 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T277",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1208,
        "fields": {
            "title": "算法提高 3000米排名预测",
            "description": r"<br />　　3000米长跑时，围观党们兴高采烈地预测着最后的排名。因为他们来自不同的班，对所有运动员不一定都了解，于是他们分别对自己了解的一些运动员的实力作出了评估，即对部分运动员做了相对排名的预测，并且告诉了可怜留守的班长。因为无聊，于是他们就组团去打Dota去了。比赛结束后他们向班长询问最后的排名，但班长不记得了，只记得他们中哪些人的预测是正确的，哪些人的预测是错误的。他们想知道比赛的排名可能是什么。",
            "input_description": r"输入描述:<br />　　第一行两个整数n， m，n为运动员数量，m为围观党数量。运动员编号从0到n-1。<br /> 　　接下来m行，每行为一个围观党的相对排名预测。每行第一个数c表示他预测的人数，后面跟着c个0~n-1的不同的数，表示他预测的运动员相对排名，最后还有一个数，0表示这个预测是错误的，1表示是正确的。 <br />输入样例: <br />Input Sample 1:<br /> 3 2<br /> 2 0 1 1<br /> 2 1 2 0<br /> <br /> Input Sample 2:<br /> 3 2<br /> 2 0 1 1<br /> 2 2 1 0",
            "output_description": r"<br />输出描述: <br />　　第一行一个数k为有多少种排名的可能。<br /> 　　下面k行，每行一个0~n-1的排列，为某一个可能的排名，相邻的数间用空格隔开。所有排名按字典序依次输出。<br /> 输出样例: <br />Output Sample 1:<br /> 2<br /> 0 2 1<br /> 2 0 1<br /> <br /> Output Sample 2:<br /> 1<br /> 0 1 2",

            "test_case_id": "2794006249936",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=n&lt;=10, 2&lt;=c&lt;=n, 1&lt;=m&lt;=10，保证数据合法，且答案中排名可能数不超过20000。对于一个排名序列，一个预测是正确的，当且仅当预测的排名的相对顺序是排名序列的一个子序列。一个预测是错误的，当且仅当这个预测不正确。",
            "create_time": "2018-03-28T03:15:44.209Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 279 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T279",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1211,
        "fields": {
            "title": "算法提高 种树",
            "description": r"<br />　　种树",
            "input_description": r"输入描述:<br />　　A城市有一个巨大的圆形广场，为了绿化环境和净化空气，市政府决定沿圆形广场外圈种一圈树。园林部门 得到指令后，初步规划出n个种树的位置，顺时针编号1到n。并且每个位置都有一个美观度Ai，如果在这里种树就可以得到这Ai的美观度。但由于A城市土壤 肥力欠佳，两棵树决不能种在相邻的位置（i号位置和i+1号位置叫相邻位置。值得注意的是1号和n号也算相邻位置！）。<br /> 　　最终市政府给园林部门提供了m棵树苗并要求全部种上，请你帮忙设计种树方案使得美观度总和最大。如果无法将m棵树苗全部种上，给出无解信息。 <br />输入样例: <br />7 3<br /> 1 2 3 4 5 6 7",
            "output_description": r"<br />输出描述: <br />　　输入的第一行包含两个正整数n、m。<br /> 　　第二行n个整数Ai。<br /> 输出样例: <br />15",

            "test_case_id": "2824064032387",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　输出一个整数，表示最佳植树方案可以得到的美观度。如果无解输出“Error!”，不包含引号。",
            "create_time": "2018-03-28T03:15:44.212Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 282 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T282",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1212,
        "fields": {
            "title": "算法提高 开灯游戏",
            "description": r"<br />　　有9盏灯与9个开关，编号都是1~9。<br /> <br /> 　　每个开关能控制若干盏灯，按下一次会改变其控制的灯的状态(亮的变成不亮，不亮变成亮的)。<br /> <br /> 　　具体如下：<br /> <br /> 　　第一个开关控制第二，第四盏灯；<br /> <br /> 　　第二个开关控制第一，第三，第五盏灯；<br /> <br /> 　　第三个开关控制第二，第六盏灯；<br /> <br /> 　　第四个开关控制第一，第五，第七盏灯；<br /> <br /> 　　第五个开关控制第二，第四，第六，第八盏灯；<br /> <br /> 　　第六个开关控制第三，第五，第九盏灯；<br /> <br /> 　　第七个开关控制第四，第八盏灯；<br /> <br /> 　　第八个开关控制第五，第七，第九盏灯；<br /> <br /> 　　第九个开关控制第六，第八盏灯。<br /> <br /> 　　开始时所有灯都是熄灭的，开关是关闭着的。要求按下若干开关后，使得只有4盏灯亮着。",
            "input_description": r"输入描述:<br />　　输出所有可能的方案，每行一个方案，每一行有9个字符，从左往右第i个字符表示第i个开关的状态(\"0\"表示关闭，\"1\"表示打开)，按字典序输出。下面的样例输出只是部分方案。 <br />输入样例: <br />000001011<br /> 000001110<br /> 000001111",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2834083293204",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.213Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 283 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T283",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1213,
        "fields": {
            "title": "算法提高 棋盘多项式",
            "description": r"<br />　　<br /> 　　棋盘多项式",
            "input_description": r"输入描述:<br />　　八皇后问题是在棋盘上放皇后，互相不攻击，求方案。变换一下棋子，还可以有八车问题，八马问题，八兵问题，八王问题，注意别念反。在这道题里，棋子换成车，同时棋盘也得换，确切说，是进行一些改造。比如现在有一张n*n的棋盘，我们在一些格子上抠几个洞，这些洞自然不能放棋子了，会漏下去的。另外，一个车本来能攻击和它的同行同列。现在，你想想，在攻击的过程中如果踩到一个洞，便会自取灭亡。故，车的攻击范围止于洞。<br /> 　　此题，给你棋盘的规模n，以及挖洞情况，求放k个车的方案数(k从0到最多可放车数) <br />输入样例: <br />3<br /> 1 0 1<br /> 1 1 1<br /> 1 0 1",
            "output_description": r"<br />输出描述: <br />　　第一行一个整数n表示棋盘大小<br /> 　　接下来n行，每行n个用空格隔开的数字0或1，0的形状表示洞，1表示没有洞<br /> 输出样例: <br />7<br /> 12<br /> 4",

            "test_case_id": "2854102554021",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　若干行，第i行表示放i个车的方案数",
            "create_time": "2018-03-28T03:15:44.214Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 285 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T285",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1214,
        "fields": {
            "title": "算法提高 铺地毯",
            "description": r"<br />　　为了准备一个学生节，组织者在会场的一片矩形区域（可看做是平面直角坐标<br /> 　　系的第一象限）铺上一些矩形地毯。一共有n 张地毯，编号从1 到n。现在将这些地毯按照<br /> 　　编号从小到大的顺序平行于坐标轴先后铺设，后铺的地毯覆盖在前面已经铺好的地毯之上。<br /> 　　地毯铺设完成后，组织者想知道覆盖地面某个点的最上面的那张地毯的编号。注意：在矩形<br /> 　　地毯边界和四个顶点上的点也算被地毯覆盖。",
            "input_description": r"输入描述:<br />　　输入共 n+2 行。<br /> 　　第一行，一个整数 n，表示总共有n 张地毯。<br /> 　　接下来的 n 行中，第i+1 行表示编号i 的地毯的信息，包含四个正整数a，b，g，k，每<br /> 　　两个整数之间用一个空格隔开，分别表示铺设地毯的左下角的坐标（a，b）以及地毯在x<br /> 　　轴和y 轴方向的长度。<br /> 　　第 n+2 行包含两个正整数x 和y，表示所求的地面的点的坐标（x，y）。 <br />输入样例: <br />3<br /> 1 0 2 3<br /> 0 2 3 3<br /> 2 1 3 3<br /> 2 2",
            "output_description": r"<br />输出描述: <br />　　输出共 1 行，一个整数，表示所求的地毯的编号；若此处没有被地毯覆盖则输出-1。<br /> 输出样例: <br />3",

            "test_case_id": "2884121814838",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于 30%的数据，有n≤2；<br /> 　　对于 50%的数据，0≤a, b, g, k≤100；<br /> 　　对于 100%的数据，有0≤n≤10,000，0≤a, b, g, k≤100,000。<br /> <br /> <br /> <br /> 　　1 0 2 3<br /> 　　0 2 3 3<br /> 　　2 1 3 3<br /> 　　4 5",
            "create_time": "2018-03-28T03:15:44.215Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 288 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T288",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1215,
        "fields": {
            "title": "算法提高 计算器",
            "description": r"<br /><b>【问题描述】</b><br /> 　　王小二的计算器上面的LED显示屏坏掉了，于是他找到了在计算器维修与应用系学习的你来为他修计算器。<br /> 　　屏幕上可以显示0~9的数字，其中每个数字由7个小二极管组成，各个数字对应的表示方式如图所示：<br /> <img width=\"426\" height=\"77\" src=\"/RequireFile.do?fid=aYT2ERHR\" /><br /> 　　。<br /> <br /> 　　为了排除电路故障，现在你需要计算，将数字A变为数字B需要经过多少次变换？<br /> 　　注意：现在将其中每段小二极管的开和关都定义为一次变换。例如数字1变为2是5次操作。<br /> <br /> <b>【输入格式】</b><br /> 　　第一行为一个正整数L，表示数码的长度。<br /> 　　接下来两行是两个长度为L的数字A和B，表示要把数字A变成数字B（数字可以以0开头）。<br /> <b>【输出格式】</b><br /> 　　一行一个整数，表示这些小二极管一共要变换多少次。<br /> <b>【样例输入1】</b><br /> <br /> 　　3<br /> 　　101<br /> 　　025<br /> <b>【样例输出1】</b><br /> 　　12<br /> <b> 【样例输入2】</b><b><br /> </b><br /> 　　8<br /> 　　19920513<br /> 　　20111211<br /> <b>【样例输出2</b><b>】</b><br /> 　　27<br /> <br /> <b>【数据范围】</b><br /> 　　L&lt;=100",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "2894141075655",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.216Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 289 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T289",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1217,
        "fields": {
            "title": "算法提高 排队打水问题",
            "description": r"<br />　　有n个人排队到r个水龙头去打水，他们装满水桶的时间t1、t2………..tn为整数且各不相等，应如何安排他们的打水顺序才能使他们总共花费的时间最少？",
            "input_description": r"输入描述:<br />　　第一行n，r (n&lt;=500,r&lt;=75)<br /> 　　第二行为n个人打水所用的时间Ti (Ti&lt;=100)； <br />输入样例: <br />3 2<br /> 1 2 3",
            "output_description": r"<br />输出描述: <br />　　最少的花费时间<br /> 输出样例: <br />",

            "test_case_id": "2924179597289",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　其中80%的数据保证n&lt;=10",
            "create_time": "2018-03-28T03:15:44.218Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 292 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T292",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1218,
        "fields": {
            "title": "算法提高 特殊的质数肋骨",
            "description": r"<br />　　农民约翰母牛总是产生最好的肋骨。你能通过农民约翰和美国农业部标记在每根肋骨上的数字认出它们。农民约翰确定他卖给买方的是真正的质数肋骨，是因为从右边开始切下肋骨，每次还剩下的肋骨上的数字都组成一个质数。<br /> <br /> 　　例如有四根肋骨的数字分别是：7 3 3 1，那么全部肋骨上的数字 7331是质数；三根肋骨 733是质数；二根肋骨 73 是质数；当然,最后一根肋骨 7 也是质数。7331 被叫做长度 4 的特殊质数。<br /> <br /> 　　写一个程序对给定的肋骨的数目 N (1&lt;=N&lt;=8),求出所有的特殊质数。数字1不被看作一个质数。",
            "input_description": r"输入描述:<br />　　单独的一行包含N。 <br />输入样例: <br />4",
            "output_description": r"<br />输出描述: <br />　　按顺序输出长度为 N 的特殊质数,每行一个。<br /> 输出样例: <br />2333<br /> 2339<br /> 2393<br /> 2399<br /> 2939<br /> 3119<br /> 3137<br /> 3733<br /> 3739<br /> 3793<br /> 3797<br /> 5939<br /> 7193<br /> 7331<br /> 7333<br /> 7393",

            "test_case_id": "2934198858106",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.219Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 293 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T293",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1223,
        "fields": {
            "title": "算法提高 产生数",
            "description": r"<br />　　<b>问题描述<br /> </b><br /> 　　给出一个整数 n（n&lt;10^30) 和 k 个变换规则（k&lt;=15）。<br /> <br /> 　　规则：<br /> <br /> 　　一位数可变换成另一个一位数：<br /> <br /> 　　规则的右部不能为零。<br /> <br /> 　　例如：n=234。有规则（k＝2）：<br /> <br /> 　　2－&gt; 5<br /> <br /> 　　3－&gt; 6<br /> <br /> 　　上面的整数 234 经过变换后可能产生出的整数为（包括原数）:<br /> <br /> 　　234<br /> <br /> 　　534<br /> <br /> 　　264<br /> <br /> 　　564<br /> <br /> 　　共 4 种不同的产生数<br /> <br /> 　　问题：<br /> <br /> 　　给出一个整数 n 和 k 个规则。<br /> <br /> 　　求出：<br /> <br /> 　　经过任意次的变换（0次或多次），能产生出多少个不同整数。<br /> <br /> 　　仅要求输出个数。<br /> 　　<b>输入格式</b>:<br /> 　　n k<br /> 　　x1 y1<br /> 　　x2 y2<br /> 　　... ...<br /> 　　xn yn<br /> 　　<b>输出格式</b>:<br /> 　　一个整数（满足条件的个数）：",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />234 2<br /> 2 5<br /> 3 6",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />4",

            "test_case_id": "3014295162191",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.224Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 301 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T301",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1225,
        "fields": {
            "title": "算法提高 数的划分",
            "description": r"<br />　　一个正整数可以划分为多个正整数的和，比如n=3时：<br /> 　　3；1＋2；1＋1＋1；<br /> 　　共有三种划分方法。<br /> 　　给出一个正整数，问有多少种划分方法。",
            "input_description": r"输入描述:<br />　　一个正整数n <br />输入样例: <br />3",
            "output_description": r"<br />输出描述: <br />　　一个正整数，表示划分方案数<br /> 输出样例: <br />3",

            "test_case_id": "3044333683825",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　n&lt;=100",
            "create_time": "2018-03-28T03:15:44.226Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 304 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T304",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1226,
        "fields": {
            "title": "算法提高 质数的后代",
            "description": r"<br />　　在上一季里，曾提到过质数的孤独，其实从另一个角度看，无情隔膜它们的合数全是质数的后代，因为合数可以由质数相乘结合而得。<br /> 　　如果一个合数由两个质数相乘而得，那么我们就叫它是质数们的直接后代。现在，给你一系列自然数，判断它们是否是质数的直接后代。",
            "input_description": r"输入描述:<br />　　第一行一个正整数T，表示需要判断的自然数数量<br /> 　　接下来T行，每行一个要判断的自然数 <br />输入样例: <br />4<br /> 3<br /> 4<br /> 6<br /> 12",
            "output_description": r"<br />输出描述: <br />　　共T行，依次对于输入中给出的自然数，判断是否为质数的直接后代，是则输出Yes，否则输出No<br /> 输出样例: <br />No<br /> Yes<br /> Yes<br /> No",

            "test_case_id": "3054352944642",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=T&lt;=20<br /> 　　2&lt;=要判断的自然数&lt;=10<sup>5</sup>",
            "create_time": "2018-03-28T03:15:44.227Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 305 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T305",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1227,
        "fields": {
            "title": "算法提高 分分钟的碎碎念",
            "description": r"<br />　　以前有个孩子，他分分钟都在碎碎念。不过，他的念头之间是有因果关系的。他会在本子里记录每一个念头，并用箭头画出这个念头的来源于之前的哪一个念头。翻开这个本子，你一定会被互相穿梭的箭头给搅晕，现在他希望你用程序计算出这些念头中最长的一条因果链。<br /> 　　将念头从1到n编号，念头i来源于念头from[i]，保证from[i]&lt;i，from[i]=0表示该念头没有来源念头，只是脑袋一抽，灵光一现。",
            "input_description": r"输入描述:<br />　　第一行一个正整数n表示念头的数量<br /> 　　接下来n行依次给出from[1]，from[2]，…，from[n] <br />输入样例: <br />8<br /> 0<br /> 1<br /> 0<br /> 3<br /> 2<br /> 4<br /> 2<br /> 4",
            "output_description": r"<br />输出描述: <br />　　共一行，一个正整数L表示最长的念头因果链中的念头数量<br /> 输出样例: <br />3",

            "test_case_id": "3074372205459",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　最长的因果链有：<br /> 　　1-&gt;2-&gt;5 (from[5]=2,from[2]=1,from[1]=0)<br /> 　　1-&gt;2-&gt;7 (from[7]=2,from[2]=1,from[1]=0)<br /> 　　3-&gt;4-&gt;6 (from[6]=4,from[4]=3,from[3]=0)<br /> 　　3-&gt;4-&gt;8 (from[8]=4,from[4]=3,from[3]=0)",
            "create_time": "2018-03-28T03:15:44.228Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 307 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T307",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1228,
        "fields": {
            "title": "算法提高 现代诗如蚯蚓",
            "description": r"<br />　　现代诗如蚯蚓<br /> 　　断成好几截都不会死<br /> 　　字符串断成好几截<br /> 　　有可能完全一样<br /> 　　请编写程序<br /> 　　输入字符串<br /> 　　输出该字符串最多能断成多少截完全一样的子串",
            "input_description": r"输入描述:<br />　　一行，一个字符串 <br />输入样例: <br />abcabcabcabc",
            "output_description": r"<br />输出描述: <br />　　一行，一个正整数表示该字符串最多能断成的截数<br /> 输出样例: <br />4",

            "test_case_id": "3084391466276",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　最多能断成四个”abc”，也就是abc重复四遍便是原串<br /> 　　同时也能断成两个”abcabc”<br /> 　　最坏情况是断成一个原串”abcabcabcabc”",
            "create_time": "2018-03-28T03:15:44.229Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 308 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T308",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1230,
        "fields": {
            "title": "算法提高 高精度乘法",
            "description": r"<br />　　在C/C++语言中，整型所能表示的范围一般为-2<sup>31</sup>到2<sup>31</sup>（大约21亿）,即使long long型，一般也只能表示到-2<sup>63</sup>到2<sup>63</sup>。要想计算更加规模的数，就要用软件来扩展了，比如用数组或字符串来模拟更多规模的数及共运算。<br /> 　　现在输入两个整数，请输出它们的乘积。",
            "input_description": r"输入描述:<br />　　两行，每行一个正整数，每个整数不超过10000位 <br />输入样例: <br />99<br /> 101",
            "output_description": r"<br />输出描述: <br />　　一行，两个整数的乘积。<br /> 输出样例: <br />9999",

            "test_case_id": "3114429987910",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　每个整数不超过10000位",
            "create_time": "2018-03-28T03:15:44.231Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 311 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T311",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1232,
        "fields": {
            "title": "算法提高 题目 2 密码锁",
            "description": r"<br />　　你获得了一个据说是古代玛雅人制作的箱子。你非常想打开箱子看看里面有什么东西,但是不幸的是,正如所有故事里一样,神秘的箱子出现的时候总是会挂着神秘的锁。<br /> 　　这个锁上面看起来有 <i>N</i> 个数字,它们排成一排,并且每个数字都在 0 到 2 之间。你发现你可以通过锁上的机关来交换<b>相邻</b>两个数字的顺序。比如,如果原来有 5 个数字 02120,在一次交换以后你就可以得到 20120,01220,02210 或者 02102。<br /> 　　根据你所搜集的情报,这个锁在上面存在某连续四个数字是“2012”的时候会自动打开。现在,你需要计算一下,你至少需要进行多少次交换操作才能打开这把锁?",
            "input_description": r"输入描述:<br />　　输入数据的第一行有一个正整数 <i>N</i>。(4 ≤ <i>N</i> ≤ 13) 输入数据的第二行有 <i>N</i> 个数字 <i>a</i><sub>1</sub>,<i>a</i><sub>2</sub>, ..., <i>a</i><sub><i>N</i></sub> ,其中 <i>a<sub>i</sub></i> 表示这个锁上面第 i 个数字的值,满足 0 ≤ <i>a<sub>i</sub></i> ≤ 2。这些数字之间没有空格分隔。<br /> <i><i><i><i> </i></i></i></i> <br />输入样例: <br />5<br /> 02120",
            "output_description": r"<br />输出描述: <br />　　你只需要输出一个数字,即你至少需要的交换次数。如果无论如何都没有希望打开这把锁,输出 -1。<br /> 输出样例: <br />1",

            "test_case_id": "3144468509544",
            "hint": r"HINT:时间限制：1.0s  内存限制：1.0GB<br />　　把前两个数字交换以后,锁上的数字是 20120,其中存在连续四个数字2, 0, 1, 2,因此锁会打开。",
            "create_time": "2018-03-28T03:15:44.233Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 314 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T314",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1233,
        "fields": {
            "title": "算法提高 能量项链",
            "description": r"<br />　　在Mars星球上，每个Mars人都随身佩带着一串能量项链。在项链上有N颗能量珠。能量珠是一颗有头标记与尾标记的珠子，这些标记对应着某个正整数。并且，对于相邻的两颗珠子，前一颗珠子的尾标记一定等于后一颗珠子的头标记。因为只有这样，通过吸盘（吸盘是Mars人吸收能量的一种器官）的作用，这两颗珠子才能聚合成一颗珠子，同时释放出可以被吸盘吸收的能量。如果前一颗能量珠的头标记为m，尾标记为r，后一颗能量珠的头标记为r，尾标记为n，则聚合后释放的能量为m*r*n（Mars单位），新产生的珠子的头标记为m，尾标记为n。<br /> 　　需要时，Mars人就用吸盘夹住相邻的两颗珠子，通过聚合得到能量，直到项链上只剩下一颗珠子为止。显然，不同的聚合顺序得到的总能量是不同的，请你设计一个聚合顺序，使一串项链释放出的总能量最大。<br /> 　　例如：设N=4，4颗珠子的头标记与尾标记依次为(2，3) (3，5) (5，10) (10，2)。我们用记号&oplus;表示两颗珠子的聚合操作，(j&oplus;k)表示第j，k两颗珠子聚合后所释放的能量。则第4、1两颗珠子聚合后释放的能量为：<br /> 　　(4&oplus;1)=10*2*3=60。<br /> 　　这一串项链可以得到最优值的一个聚合顺序所释放的总能量为<br /> 　　((4&oplus;1)&oplus;2)&oplus;3）=10*2*3+10*3*5+10*5*10=710。",
            "input_description": r"输入描述:<br />　　输入的第一行是一个正整数N（4≤N≤100），表示项链上珠子的个数。第二行是N个用空格隔开的正整数，所有的数均不超过1000。第i个数为第i颗珠子的头标记（1≤i≤N），当i&lt;N时，第i颗珠子的尾标记应该等于第i+1颗珠子的头标记。第N颗珠子的尾标记应该等于第1颗珠子的头标记。<br /> 　　至于珠子的顺序，你可以这样确定：将项链放到桌面上，不要出现交叉，随意指定第一颗珠子，然后按顺时针方向确定其他珠子的顺序。 <br />输入样例: <br />4<br /> 2 3 5 10",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，是一个正整数E（E≤2.1*10<sup>9</sup>），为一个最优聚合顺序所释放的总能量。<br /> 输出样例: <br />710",

            "test_case_id": "3164487770361",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.234Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 316 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T316",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1234,
        "fields": {
            "title": "算法提高 超级玛丽",
            "description": r"<br />　　大家都知道\"超级玛丽\"是一个很善于跳跃的探险家，他的拿手好戏是跳跃，但它一次只能向前跳一步或两步。有一次，他要经过一条长为n的羊肠小道，小道中有m个陷阱，这些陷阱都位于整数位置，分别是a<sub>1</sub>,a<sub>2</sub>,....a<sub>m</sub>，陷入其中则必死无疑。显然，如果有两个挨着的陷阱，则玛丽是无论如何也跳过不去的。<br /> 　　现在给出小道的长度n，陷阱的个数及位置。求出玛丽从位置1开始，有多少种跳跃方法能到达胜利的彼岸（到达位置n）。",
            "input_description": r"输入描述:<br />　　第一行为两个整数n,m<br /> 　　第二行为m个整数，表示陷阱的位置 <br />输入样例: <br />4 1<br /> 2",
            "output_description": r"<br />输出描述: <br />　　一个整数。表示玛丽跳到n的方案数<br /> 输出样例: <br />1",

            "test_case_id": "3184507031178",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　40&gt;=n&gt;=3,m&gt;=1<br /> 　　n&gt;m;<br /> 　　陷阱不会位于1及n上",
            "create_time": "2018-03-28T03:15:44.235Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 318 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T318",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1236,
        "fields": {
            "title": "算法提高 聪明的美食家",
            "description": r"<br />　　如果有人认为吃东西只需要嘴巴，那就错了。<br /> 　　都知道舌头有这么一个特性，“由简入奢易，由奢如简难”（据好事者考究，此规律也适合许多其他情况）。具体而言，如果是甜食，当你吃的食物不如前面刚吃过的东西甜，就很不爽了。<br /> 　　大宝是一个聪明的美食家，当然深谙此道。一次他来到某小吃一条街，准备从街的一头吃到另一头。为了吃得爽，他大费周章，得到了各种食物的“美味度”。他拒绝不爽的经历，不走回头路而且还要爽歪歪（爽的次数尽量多）。",
            "input_description": r"输入描述:<br />　　两行数据。<br /> 　　第一行为一个整数n，表示小吃街上小吃的数量<br /> 　　第二行为n个整数，分别表示n种食物的“美味度” <br />输入样例: <br />10<br /> 3 18 7 14 10 12 23 41 16 24",
            "output_description": r"<br />输出描述: <br />　　一个整数，表示吃得爽的次数<br /> 输出样例: <br />6",

            "test_case_id": "3204545552812",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　美味度为0到100的整数<br /> 　　n&lt;1000",
            "create_time": "2018-03-28T03:15:44.237Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 320 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T320",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1237,
        "fields": {
            "title": "算法提高 贪吃的大嘴",
            "description": r"<br />　　有一只特别贪吃的大嘴,她很喜欢吃一种小蛋糕,而每一个小蛋糕有一个美味度,而大嘴是很傲娇的,一定要吃美味度和刚好为m的小蛋糕,而且大嘴还特别懒,她希望通过吃数量最少的小蛋糕达到这个目的.所以她希望你能设计一个程序帮她决定要吃哪些小蛋糕.",
            "input_description": r"输入描述:<br />　　先输入一行包含2个整数m、n,表示大嘴需要吃美味度和为m的小蛋糕,而小蛋糕一共有n种,下面输入n行,每行2个整数,第一个表示该种小蛋糕的美味度,第二个表示蛋糕店中该种小蛋糕的总数 <br />输入样例: <br />10 2<br /> 4 1<br /> 2 10",
            "output_description": r"<br />输出描述: <br />　　输出一行包含一个整数表示大嘴最少需要吃的小蛋糕数量,若大嘴无法通过吃小蛋糕达到m的美味度和,则输出\"&gt;&lt;“.<br /> 输出样例: <br />4",

            "test_case_id": "3224564813629",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　m ≤ 20000,小蛋糕总数量≤50.",
            "create_time": "2018-03-28T03:15:44.238Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 322 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T322",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1238,
        "fields": {
            "title": "算法提高 士兵排队问题",
            "description": r"<br />　　有Ｎ个士兵(1≤Ｎ≤26)，编号依次为Ａ,Ｂ,Ｃ,…，队列训练时，指挥官要把一些士兵从高到矮一次排成一行，但现在指挥官不能直接获得每个人的身高信息，只能获得“P1比P2高”这样的比较结果(P1、P2∈Ａ,Ｂ,Ｃ,…,Ｚ,记为 P1&gt;P2)，如”Ａ&gt;Ｂ”表示Ａ比Ｂ高。<br /> 　　请编一程序，根据所得到的比较结果求出一种符合条件的排队方案。<br /> 　　（注：比较结果中没有涉及的士兵不参加排队）",
            "input_description": r"输入描述:<br />　　比较结果从文本文件中读入（文件由键盘输入），每个比较结果在文本文件中占一行。 <br />输入样例: <br />A&gt;B<br /> B&gt;D<br /> F&gt;D",
            "output_description": r"<br />输出描述: <br />　　若输入数据无解，打印“No Answer!”信息，否则从高到矮一次输出每一个士兵的编号，中间无分割符，并把结果写入文本文件中，文件由键盘输入：<br /> 输出样例: <br />AFBD",

            "test_case_id": "3234584074446",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.239Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 323 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T323",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1239,
        "fields": {
            "title": "算法提高 数字黑洞",
            "description": r"<br />　　任意一个四位数，只要它们各个位上的数字是不全相同的，就有这样的规律：<br /> 　　1)将组成该四位数的四个数字由大到小排列，形成由这四个数字构成的最大的四位数；<br /> 　　2)将组成该四位数的四个数字由小到大排列，形成由这四个数字构成的最小的四位数(如果四个数中含有0，则得到的数不足四位)；<br /> 　　3)求两个数的差，得到一个新的四位数(高位零保留)。<br /> 　　重复以上过程，最后一定会得到的结果是6174。<br /> 　　比如：4312 3087 8352 6174，经过三次变换，得到6174",
            "input_description": r"输入描述:<br />　　一个四位整数，输入保证四位数字不全相同 <br />输入样例: <br />4312",
            "output_description": r"<br />输出描述: <br />　　一个整数，表示这个数字经过多少次变换能得到6174<br /> 输出样例: <br />3",

            "test_case_id": "3244603335263",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.240Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 324 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T324",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1240,
        "fields": {
            "title": "算法提高 身份证排序",
            "description": r"<br />　　安全局搜索到了一批(n个)身份证号码，希望按出生日期对它们进行从大到小排序，如果有相同日期，则按身份证号码大小进行排序。身份证号码为18位的数字组成，出生日期为第7到第14位",
            "input_description": r"输入描述:<br />　　第一行一个整数n，表示有n个身份证号码<br /> 　　余下的n行，每行一个身份证号码。 <br />输入样例: <br />5<br /> 466272307503271156<br /> 215856472207097978<br /> 234804580401078365<br /> 404475727700034980<br /> 710351408803093165",
            "output_description": r"<br />输出描述: <br />　　按出生日期从大到小排序后的身份证号，每行一条<br /> 输出样例: <br />404475727700034980<br /> 234804580401078365<br /> 215856472207097978<br /> 710351408803093165<br /> 466272307503271156",

            "test_case_id": "3264622596080",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　n&lt;=100000",
            "create_time": "2018-03-28T03:15:44.241Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 326 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T326",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1241,
        "fields": {
            "title": "算法提高 淘淘的名单",
            "description": r"<br />　　by ZBY... :) 淘淘拿到了一份名单，他想对上面的名字进行处理，挑出一些特殊的名字，他请你来帮忙。<br /> 　　淘淘关注以下名字：<br /> 　　如果这个名字是“WYS”，他希望你的程序输出“KXZSMR”。<br /> 　　如果这个名字是“CQ”，他希望你的程序输出“CHAIQIANG”。<br /> 　　如果这个名字是“LC“，他希望你的程序输出“DRAGONNET”。<br /> 　　如果这个名字是“SYT”或“SSD”或“LSS”或“LYF”，他希望你的程序输出“STUDYFATHER”。<br /> 　　如果这个名字与上述任意名字都不相同，他希望你的程序输出“DENOMINATOR”。",
            "input_description": r"输入描述:<br />　　第一行有一个整数N，表示淘淘手中名单里的人数。<br /> 　　接下来N行，每行有一个字符串，即名单里的人名。 <br />输入样例: <br />9<br /> WYS<br /> CQ<br /> WYS<br /> LC<br /> SYT<br /> SSD<br /> LSS<br /> LYF<br /> ZBY",
            "output_description": r"<br />输出描述: <br />　　输出N行，每行输出每个人名的判断结果。<br /> 输出样例: <br />KXZSMR<br /> CHAIQIANG<br /> KXZSMR<br /> DRAGONNET<br /> STUDYFATHER<br /> STUDYFATHER<br /> STUDYFATHER<br /> STUDYFATHER<br /> DENOMINATOR",

            "test_case_id": "3274641856897",
            "hint": r"HINT:时间限制：100ms  内存限制：8.0MB<br />　　对于 50% 数据，N &lt;= 1000，且名单中的名字仅可能为“WYS”,“CQ”,“LC”三者之一，没有其他的名字。<br /> 　　对于 100% 数据，N &lt;= 10000，人名仅由大写字母组成，长度不超过5。",
            "create_time": "2018-03-28T03:15:44.242Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 327 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T327",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1242,
        "fields": {
            "title": "算法提高 输入输出格式练习",
            "description": r"<br />　　按格式格式读入一个3位的整数、一个实数、一个字符 。<br /> 　　并按格式输出 一个整数占8位左对齐、一个实数占8位右对齐、一个字符 ，并用|隔开。",
            "input_description": r"输入描述:<br />　　见题面 <br />输入样例: <br />123456.789|a",
            "output_description": r"<br />输出描述: <br />　　见题面<br /> 输出样例: <br />123     |   456.8|a",

            "test_case_id": "3284661117714",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.243Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 328 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T328",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1243,
        "fields": {
            "title": "算法提高 陶陶摘苹果",
            "description": r"<br />　　陶陶家的院子里有一棵苹果树，每到秋天树上就会结出n个苹果。苹果成熟的时候，陶陶就会跑去摘苹果。陶陶有个30厘米高的板凳，当她不能直接用手摘到苹果的时候，就会踩到板凳上再试试。<br /> 　　现在已知n个苹果到地面的高度，以及陶陶把手伸直的时候能够达到的最大高度，请帮陶陶算一下她能够摘到的苹果的数目。假设她碰到苹果，苹果就会掉下来。",
            "input_description": r"输入描述:<br />　　输入包括两行数据。第一行只包括两个正整数n(5&lt;=n&lt;=200)和m(100&lt;=m&lt;=150),表示苹果数目和桃桃伸手可达到的高度（以厘米为单位）。第二行包含n个100到200之间（包括100和200）的整数（以厘米为单位）分别表示苹果到地面的高度，两个相邻的整数之间用一个空格隔开。 <br />输入样例: <br />10 110<br /> <br /> <br /> 100 200 150 140 129 134 167 198 200 111",
            "output_description": r"<br />输出描述: <br />　　输出包括一行，这一行只包含一个整数，表示陶陶能够摘到的苹果的数目。<br /> 输出样例: <br />5<br /> ",

            "test_case_id": "3304680378531",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.244Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 330 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T330",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1244,
        "fields": {
            "title": "算法提高 理财计划",
            "description": r"<br />　　银行近期推出了一款新的理财计划“重复计息储蓄”。储户只需在每个月月初存入固定金额的现金，银行就会在每个月月底根据储户账户内的金额算出该月的利息并将利息存入用户账号。现在如果某人每月存入k元，请你帮他计算一下，n月后，他可以获得多少收益。",
            "input_description": r"输入描述:<br />　　输入数据仅一行，包括两个整数k(100&lt;=k&lt;=10000)、n(1&lt;=n&lt;=48)和一个小数p(0.001&lt;=p&lt;=0.01)，分别表示每月存入的金额、存款时长、存款利息。 <br />输入样例: <br />1000 6 0.01",
            "output_description": r"<br />输出描述: <br />　　输出数据仅一个数，表示可以得到的收益。<br /> 输出样例: <br />213.53",

            "test_case_id": "3314699639348",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.245Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 331 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T331",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1245,
        "fields": {
            "title": "算法提高 解二元一次方程组",
            "description": r"<br />　　给定一个二元一次方程组，形如：<br /> 　　a * x + b * y = c;<br /> 　　d * x + e * y = f;<br /> 　　x,y代表未知数，a, b, c, d, e, f为参数。<br /> 　　求解x,y",
            "input_description": r"输入描述:<br />　　输入包含六个整数: a, b, c, d, e, f; <br />输入样例: <br />例：<br /> 3 7 41 2 1 9",
            "output_description": r"<br />输出描述: <br />　　输出为方程组的解，两个整数x, y。<br /> 输出样例: <br />例：<br /> 2 5",

            "test_case_id": "3334718900165",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　0 &lt;= a, b, c, d, e, f &lt;= 2147483647",
            "create_time": "2018-03-28T03:15:44.246Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 333 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T333",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1247,
        "fields": {
            "title": "算法提高 陶陶摘苹果2",
            "description": r"<br />　　陶陶家的院子里有一棵苹果树，每到秋天树上就会结出n个苹果。苹果成熟的时候，陶陶就会跑去摘苹果。陶陶有个30厘米高的板凳，当她不能直接用手摘到苹果的时候，就会踩到板凳上再试试。<br /> 　　现在已知n个苹果到地面的高度，以及陶陶把手伸直的时候能够达到的最大高度。假设她碰到苹果，苹果就会掉下来。请帮陶陶算一下,经过她的洗劫后，苹果树上还有几个苹果。",
            "input_description": r"输入描述:<br />　　输入包括两行数据。第一行只包括两个正整数n(5&lt;=n&lt;=200)和m(60&lt;=m&lt;=200),表示苹果数目和桃桃伸手可达到的高度（以厘米为单位）。第二行包含n个100到200之间（包括100和200）的整数（以厘米为单位）分别表示苹果到地面的高度，两个相邻的整数之间用一个空格隔开。 <br />输入样例: <br />10 110<br /> 100 200 150 140 129 134 167 198 200 111",
            "output_description": r"<br />输出描述: <br />　　输出包括一行，这一行只包含一个整数，表示陶陶不能够摘到的苹果的数目。<br /> 输出样例: <br />5<br /> ",

            "test_case_id": "3374757421799",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.248Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 337 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T337",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1250,
        "fields": {
            "title": "算法提高 质因数2",
            "description": r"<br />　　将一个正整数N(1&lt;N&lt;32768)分解质因数，把质因数按从小到大的顺序输出。最后输出质因数的个数。",
            "input_description": r"输入描述:<br />　　一行，一个正整数 <br />输入样例: <br />66",
            "output_description": r"<br />输出描述: <br />　　两行，第一行为用空格分开的质因数<br /> 　　第二行为质因数的个数<br /> 输出样例: <br />2 3 113",

            "test_case_id": "3414815204250",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.251Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 341 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T341",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1251,
        "fields": {
            "title": "算法提高 前10名",
            "description": r"<br />　　数据很多，但我们经常只取前几名，比如奥运只取前3名。现在我们有n个数据，请按从大到小的顺序，输出前10个名数据。",
            "input_description": r"输入描述:<br />　　两行。<br /> 　　第一行一个整数n，表示要对多少个数据<br /> 　　第二行有n个整数，中间用空格分隔。表示n个数据。 <br />输入样例: <br />26<br /> 54 27 87 16 63 40 40 22 61 6 57 70 0 42 11 50 13 5 56 7 8 86 56 91 68 59",
            "output_description": r"<br />输出描述: <br />　　一行，按从大到小排列的前10个数据，每个数据之间用一个空格隔开。<br /> 输出样例: <br />91 87 86 70 68 63 61 59 57 56",

            "test_case_id": "3424834465067",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　10&lt;=n&lt;=200,各个整数不超出整型范围",
            "create_time": "2018-03-28T03:15:44.252Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 342 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T342",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1253,
        "fields": {
            "title": "算法提高 分苹果",
            "description": r"<br />　　小朋友排成一排，老师给他们分苹果。<br /> 　　小朋友从左到右标号1..N。有M个老师，每次第i个老师会给第Li个到第Ri个，一共Ri-Li+1个小朋友每人发Ci个苹果。<br /> 　　最后老师想知道每个小朋友有多少苹果。",
            "input_description": r"输入描述:<br />　　第一行两个整数N、M，表示小朋友个数和老师个数。<br /> 　　接下来M行，每行三个整数Li、Ri、Ci，意义如题目表述。 <br />输入样例: <br />5 3<br /> 1 2 1<br /> 2 3 2<br /> 2 5 3",
            "output_description": r"<br />输出描述: <br />　　一行N个数，第i个数表示第i个小朋友手上的水果。<br /> 输出样例: <br />1 6 5 3 3",

            "test_case_id": "3454872986701",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　40%的数据，N、M≤1 000。<br /> 　　100%的数据，N、M≤100 000，1≤Li≤Ri≤N，0≤Ci≤100。",
            "create_time": "2018-03-28T03:15:44.254Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 345 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T345",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1255,
        "fields": {
            "title": "算法提高 素数求和",
            "description": r"<br />　　﻿输入一个自然数n，求小于等于n的素数之和",
            "input_description": r"输入描述:<br />　　测试样例保证 2 &lt;= n &lt;= 2,000,000 <br />输入样例: <br />2",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />2",

            "test_case_id": "3484911508335",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.256Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 348 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T348",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1256,
        "fields": {
            "title": "算法提高 五次方数",
            "description": r"<br />　　对一个数十进制表示时的每一位数字乘五次方再求和，会得到一个数的五次方数<br /> 　　例如：1024的五次方数为1+0+32+1024=1057<br /> 　　有这样一些神奇的数，它的五次方数就是它自己，而且这样的数竟然只有有限多个<br /> 　　从小到大输出所有这样的数",
            "input_description": r"输入描述:<br />　　每个数独立一行输出 <br />输入样例: <br />10<br /> 200<br /> 3000",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3494930769152",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.257Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 349 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T349",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1257,
        "fields": {
            "title": "算法提高 排列式",
            "description": r"<br />　　7254是一个不寻常的数，因为它可以表示为7254 = 39 x 186，这个式子中1~9每个数字正好出现一次<br /> 　　输出所有这样的不同的式子（乘数交换被认为是相同的式子）<br /> 　　结果小的先输出；结果相同的，较小的乘数较小的先输出。",
            "input_description": r"输入描述:<br />　　每一行输出一个式子，式子中的等号前后空格、乘号（用字母x代表）前后空格<br /> 　　较小的乘数写在前面 <br />输入样例: <br />问题中的式子在结果中会出现一行如下：<br /> 7254 = 39 x 186",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3504950029969",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.258Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 350 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T350",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1258,
        "fields": {
            "title": "算法提高 勾股数",
            "description": r"<br />　　勾股数是一组三个自然数，a &lt; b &lt; c，以这三个数为三角形的三条边能够形成一个直角三角形<br /> 　　输出所有a + b + c &lt;= 1000的勾股数<br /> 　　a小的先输出；a相同的，b小的先输出。",
            "input_description": r"输入描述:<br />　　每行为一组勾股数，用空格隔开 <br />输入样例: <br />例如，结果的前三行应当是<br /> 3 4 5<br /> 5 12 13<br /> 6 8 10",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3514969290786",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.259Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 351 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T351",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1259,
        "fields": {
            "title": "算法提高 连接乘积",
            "description": r"<br />　　192这个数很厉害，用它分别乘以1、2、3，会得到：<br /> 　　192 x 1 = 192<br /> 　　192 x 2 = 384<br /> 　　192 x 3 = 576<br /> 　　把这三个乘积连起来，得到192384576，正好是一个1~9的全排列<br /> 　　我们把上面的运算定义为连接乘积：<br /> 　　m x (1 ... n) = k（其中m &gt; 0 且 n &gt; 1，对于上例，m = 192、n = 3、k = 192384576）<br /> 　　即k是把m分别乘以1到n的乘积连接起来得到的，则称k为m和n的连接乘积。<br /> 　　按字典序输出所有不同的连接乘积k，满足k是1~9的全排列",
            "input_description": r"输入描述:<br />　　每个k占一行 <br />输入样例: <br />显然，结果中应包含一行：<br /> 192384576",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3534988551603",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.260Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 353 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T353",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1260,
        "fields": {
            "title": "算法提高 师座操作系统",
            "description": r"<br />　　师座这天在程序设计课上学了指针和结构体以后，觉得自己可以轻松的写出操作系统，为了打败大微软帝国，他给这个系统起了个响亮的名字“操师座系统”，你是师座手下的首席架构师，被要求写这个操作系统的文件系统部分，要求如下：<br /> 　　这个文件系统有的所有文件都有一个独一无二的文件名，除此之外分为两类文件，一类文件是数据存储文件，它可以存储一个字符串信息，另一类文件是快捷方式，它会指向另一个文件，有可能是数据块也有可能是快捷方式。<br /> 　　.<br /> 　　这个文件系统支持3条命令：<br /> 　　1.创建命令：create &lt;FileName&gt; &lt;FileType&gt; &lt;FileInfo&gt;<br /> 　　这个命令的意思是，创建一个文件名为&lt;FileName&gt;，文件类型为&lt;FileType&gt;，文件信息为&lt;FileInfo&gt;，文件类型为0或者1,0表示数据块，1表示快捷方式，如果是数据块，那么&lt;FileInfo&gt;表示储存的字符串，如果这是一个快捷方式，&lt;FileInfo&gt;表示指向的文件的名称，如果当前已存在名为&lt;FileName&gt;的文件，则更新这个文件的信息。<br /> 　　.<br /> 　　2.打开命令：open &lt;FileName&gt;<br /> 　　这个命令是打开文件名为&lt;FileName&gt;的文件，如果这是一个快捷方式，则会打开这个快捷方式指向的文件，直到打开一个数据块时，显示这个数据块储存的信息并换行。<br /> 　　.<br /> 　　3.退出命令：exit<br /> 　　得到这个命令以后，你的程序需要安全终止。",
            "input_description": r"输入描述:<br />　　若干条命令构成，最后一条命令必然为exit。 <br />输入样例: <br />create shizuo 0 lu<br /> create lyf 0 luoyuf<br /> create p1 1 shizuo<br /> open p1<br /> create p2 1 p1<br /> open p2<br /> create p1 1 lyf<br /> open p2<br /> exit",
            "output_description": r"<br />输出描述: <br />　　输出每次使用open命令的显示结果。<br /> 输出样例: <br />lu<br /> lu<br /> <br /> luoyuf",

            "test_case_id": "3545007812420",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　总命令条数不超过1000条。<br /> 　　保证&lt;FileName&gt;，&lt;FileType&gt;，&lt;FileInfo&gt;不包含空格和不合法字符，每个长度不超过20个字符。",
            "create_time": "2018-03-28T03:15:44.261Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 354 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T354",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1263,
        "fields": {
            "title": "算法提高 洗牌",
            "description": r"<br />　　小弱T在闲暇的时候会和室友打扑克，输的人就要负责洗牌。虽然小弱T不怎么会洗牌，但是他却总是输。<br /> 　　渐渐地小弱T发现了一个规律：只要自己洗牌，自己就一定会输。所以小弱T认为自己洗牌不够均匀，就独创了一种小弱洗牌法。<br /> 　　小弱洗牌法是这样做的：先用传统洗牌法将52张扑克牌（1到K各四张，除去大小王）打乱，放成一堆，然后每次从牌堆顶层拿一张牌。如果这张牌的大小是P（1到K的大小分别为1到13），那么就把这张牌插入到当前手中第P张牌的后面。如果当前手中不足P张牌，那么就把这张牌放在最后。<br /> 　　现在给你一对已经被打乱的牌，请你用小弱洗牌法进行洗牌，然后输出最后生成的序列。<br /> 　　注意：小弱可能在第一次洗牌时弄丢了某些牌，这时请你输出一个-1来提醒他牌的数目不够。",
            "input_description": r"输入描述:<br />　　测试数据的输入含N个用空格隔开的字符串表示牌堆从顶至底的每张扑克（1到K中的某个）。可能有多行。 <br />输入样例: <br />4 6 K Q 5 1 Q 9 7 9 K 3 J 1 2 3 5<br /> 2<br /> 3 5 7 Q 7 10 8 4 9 7 8 9 4<br /> 10 6 2 8 2 10 10 Q 5 K J 1<br /> J 8 3 K 4 1 6 J 6",
            "output_description": r"<br />输出描述: <br />　　如果N为52，输出用小弱洗牌法洗牌后的序列，每个字符串用空格隔开。<br /> 　　否则请输出一个-1.<br /> 输出样例: <br />4 1 1 1 3 4 6 6 2 2 2 5 J 3 8 4 4 6 K J 8 J 10 10 K Q 2 5 7 8 10 9 3 7 9 8 7 1 10 5 6 3 Q K Q 5 Q 7 9 9 J K",

            "test_case_id": "3585065594871",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　保证每个字符串都为1 2 3 4 5 6 7 8 9 10 J Q K中的一个。",
            "create_time": "2018-03-28T03:15:44.264Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 358 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T358",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1264,
        "fields": {
            "title": "算法提高 盾神与砝码称重",
            "description": r"<br />　　有一天，他在宿舍里无意中发现了一个天平！这个天平很奇怪，有n个完好的砝码，但是没有游码。盾神为他的发现兴奋不已！于是他准备去称一称自己的东西。他准备好了m种物品去称。神奇的是，盾神一早就知道这m种物品的重量，他现在是想看看这个天平能不能称出这些物品出来。但是盾神稍微想了1秒钟以后就觉得这个问题太无聊了，于是就丢给了你。",
            "input_description": r"输入描述:<br />　　第一行为两个数，n和m。<br /> 　　第二行为n个数，表示这n个砝码的重量。<br /> 　　第三行为m个数，表示这m个物品的重量。 <br />输入样例: <br />4 2<br /> 1 2 4 8<br /> 15 16",
            "output_description": r"<br />输出描述: <br />　　输出m行，对于第i行，如果第i个物品能被称出，输出YES否则输出NO。<br /> 输出样例: <br />YES<br /> NO",

            "test_case_id": "3595084855688",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=n&lt;=24, 1&lt;=m&lt;=10.",
            "create_time": "2018-03-28T03:15:44.265Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 359 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T359",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1265,
        "fields": {
            "title": "算法提高 盾神与积木游戏",
            "description": r"<br />　　最近的m天盾神都去幼儿园陪小朋友们玩去了~<br /> 　　每个小朋友都拿到了一些积木，他们各自需要不同数量的积木来拼一些他们想要的东西。但是有的小朋友拿得多，有的小朋友拿得少，有些小朋友需要拿到其他小朋友的积木才能完成他的大作。如果某个小朋友完成了他的作品，那么他就会把自己的作品推倒，而无私地把他的所有积木都奉献出来；但是，如果他还没有完成自己的作品，他是不会把积木让出去的哟~<br /> 　　盾神看到这么和谐的小朋友们感到非常开心，于是想帮助他们所有人都完成他们各自的作品。盾神现在在想，这个理想有没有可能实现呢？于是把这个问题交给了他最信赖的你。",
            "input_description": r"输入描述:<br />　　第一行为一个数m。<br /> 　　接下来有m组数据。每一组的第一行为n，表示这天有n个小朋友。接下来的n行每行两个数，分别表示他现在拥有的积木数和他一共需要的积木数。 <br />输入样例: <br />2<br /> 2<br /> 2 2<br /> 1 3<br /> 3<br /> 1 5<br /> 3 3<br /> 0 4",
            "output_description": r"<br />输出描述: <br />　　输出m行，如果第i天能顺利完成所有作品，输出YES，否则输出NO。<br /> 输出样例: <br />YES<br /> NO",

            "test_case_id": "3615104116505",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=n&lt;=10000，1&lt;=m&lt;=10。",
            "create_time": "2018-03-28T03:15:44.266Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 361 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T361",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1266,
        "fields": {
            "title": "算法提高 文化之旅",
            "description": r"<br />　　有一位使者要游历各国，他每到一个国家，都能学到一种文化，但他不愿意学习任何一种文化超过一次（即如果他学习了某种文化，则他就不能到达其他有这种文化的国家）。不同的国家可能有相同的文化。不同文化的国家对其他文化的看法不同，有些文化会排斥外来文化（即如果他学习了某种文化，则他不能到达排斥这种文化的其他国家）。<br /> 　　现给定各个国家间的地理关系，各个国家的文化，每种文化对其他文化的看法，以及这位使者游历的起点和终点（在起点和终点也会学习当地的文化），国家间的道路距离，试求从起点到终点最少需走多少路。",
            "input_description": r"输入描述:<br />　　第一行为五个整数N，K，M，S，T，每两个整数之间用一个空格隔开，依次代表国家个数（国家编号为1到N），文化种数（文化编号为1到K），道路的条数，以及起点和终点的编号（保证S不等于T）；<br /> 　　第二行为N个整数，每两个整数之间用一个空格隔开，其中第i个数C<sub>i</sub>，表示国家i的文化为C<sub>i</sub>。<br /> 　　接下来的K行，每行K个整数，每两个整数之间用一个空格隔开，记第i行的第j个数为a<sub>ij</sub>，a<sub>ij</sub>= 1表示文化i排斥外来文化j（i等于j时表示排斥相同文化的外来人），a<sub>ij</sub>= 0表示不排斥（注意i排斥j并不保证j一定也排斥i）。<br /> 　　接下来的M行，每行三个整数u，v，d，每两个整数之间用一个空格隔开，表示国家u与国家v有一条距离为d的可双向通行的道路（保证u不等于v，两个国家之间可能有多条道路）。 <br />输入样例: <br />2 2 1 1 2<br /> 1 2<br /> 0 1<br /> 1 0<br /> 1 2 10",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，一个整数，表示使者从起点国家到达终点国家最少需要走的距离数（如果无解则输出-1）。<br /> 输出样例: <br />-1",

            "test_case_id": "3625123377322",
            "hint": r"HINT:时间限制：1.0s  内存限制：128.0MB<br />　　由于到国家2必须要经过国家1，而国家2的文明却排斥国家1的文明，所以不可能到达国家2。",
            "create_time": "2018-03-28T03:15:44.267Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 362 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T362",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1267,
        "fields": {
            "title": "算法提高 摆花",
            "description": r"<br />　　小明的花店新开张，为了吸引顾客，他想在花店的门口摆上一排花，共m盆。通过调查顾客的喜好，小明列出了顾客最喜欢的n种花，从1到n标号。为了在门口展出更多种花，规定第i种花不能超过a<sub>i</sub>盆，摆花时同一种花放在一起，且不同种类的花需按标号的从小到大的顺序依次摆列。<br /> 　　试编程计算，一共有多少种不同的摆花方案。",
            "input_description": r"输入描述:<br />　　第一行包含两个正整数n和m，中间用一个空格隔开。<br /> 　　第二行有n个整数，每两个整数之间用一个空格隔开，依次表示a<sub>1</sub>、a<sub>2</sub>、……a<sub>n</sub>。 <br />输入样例: <br />2 4<br /> 3 2",
            "output_description": r"<br />输出描述: <br />　　输出只有一行，一个整数，表示有多少种方案。<b>注意：因为方案数可能很多，请输出方案数对</b><b>1000007</b><b>取模的结果。</b><br /> 输出样例: <br />2",

            "test_case_id": "3635142638139",
            "hint": r"HINT:时间限制：1.0s  内存限制：128.0MB<br />　　有2种摆花的方案，分别是(1，1，1，2)， (1，1，2，2)。括号里的1和2表示两种花，比如第一个方案是前三个位置摆第一种花，第四个位置摆第二种花。",
            "create_time": "2018-03-28T03:15:44.268Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 363 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T363",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1268,
        "fields": {
            "title": "算法提高 P1003",
            "description": r"<br />　　作为一名网络警察，你的任务是监视电子邮件，看其中是否有一些敏感的关键词。不过，有些狡猾的犯罪嫌疑人会改变某些单词的字母顺序，以逃避检查。请编写一个程序，发现这种调整过顺序的关键词。程序的输入有两行，第一行是关键词列表，第二行是待检查的句子。程序的输出为在该句子中所找到的经过顺序调整的关键词。（单词全部为小写，单词之间以一个空格分隔，每一行的单词个数不限）<br /> <br /> <b>输入：</b><br /> 　　guns mines missiles<br /> 　　aameric ssell snug dan iimsssle ot sit neeemis<br /> <b> </b><br /> <b>输出：</b><br /> 　　guns missiles",
            "input_description": r"输入描述:<br /> <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br /><br /> 输出样例: <br />",

            "test_case_id": "3655161898956",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.269Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 365 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T365",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1270,
        "fields": {
            "title": "算法提高 线段和点",
            "description": r"<br />　　有n个点和m个区间，点和区间的端点全部是整数，对于点a和区间[b,c]，若a&gt;=b且a&lt;=c，称点a满足区间[b,c]。<br /> 　　求最小的点的子集，使得所有区间都被满足。",
            "input_description": r"输入描述:<br />　　第一行两个整数n m<br /> 　　以下n行 每行一个整数，代表点的坐标<br /> 　　以下m行 每行两个整数，代表区间的范围 <br />输入样例: <br />5 5<br /> 2<br /> 6<br /> 3<br /> 8<br /> 7<br /> 2 5<br /> 3 4<br /> 3 3<br /> 2 7<br /> 6 9",
            "output_description": r"<br />输出描述: <br />　　输出一行，最少的满足所有区间的点数，如无解输出-1。<br /> 输出样例: <br />2",

            "test_case_id": "3675200420590",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　1&lt;=n,m&lt;=10000<br /> 　　0&lt;=点和区间的坐标&lt;=50000",
            "create_time": "2018-03-28T03:15:44.271Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 367 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T367",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1271,
        "fields": {
            "title": "算法提高 我们的征途是星辰大海",
            "description": r"<br />　　最新的火星探测机器人curiosity被困在了一个二维迷宫里，迷宫由一个个方格组成。<br /> 　　共有四种方格：<br /> 　　‘.’  代表空地，curiosity可以穿过它<br /> 　　‘#’ 代表障碍物，不可穿越，不可停留<br /> 　　‘S’ 代表curiosity的起始位置<br /> 　　‘T’  代表curiosity的目的地<br /> 　　NASA将会发送一系列的命令给curiosity，格式如下：“LRUD”分别代表向左，向右，向上，向下走一步。由于地球和火星之间最近时也有55000000km！所以我们必须提前判断这一系列的指令会让curiosity最终处在什么样的状态，请编程完成它。",
            "input_description": r"输入描述:<br />　　第一行是一个整数T，代表有几个测试样例<br /> 　　每个测试样例第一行是一个整数N（1&lt;=N&lt;=50））代表迷宫的大小（N*N）。随后的N行每行由N个字符串组成，代表迷宫。接下来的一行是一个整数Q，代表有多少次询问，接下来的Q行每行是一个仅由“LRUD”四个字母的组成的字符串，字符转长度小于1000. <br />输入样例: <br />",
            "output_description": r"<br />输出描述: <br />　　对于每个询问输出单独的一行：<br /> 　　“I get there!”：执行给出的命令后curiosity最终到达了终点。<br /> 　　“<b>I have no idea!</b>”：执行给出的命令后curiosity未能到达终点。<br /> 　　“I am dizzy!”：curiosity在执行命令的过程中撞到了障碍物。<br /> 　　“<b>I am out!</b>”：代表curiosity在执行命令的过程中走出了迷宫的边界。<br /> <b>Sample Input </b><br /> 　　2<br /> 　　2<br /> 　　S.<br /> 　　#T<br /> 　　2<br /> 　　RD<br /> 　　DR<br /> 　　3<br /> 　　S.#<br /> 　　.#.<br /> 　　.T#<br /> 　　3<br /> 　　RL<br /> 　　DDD<br /> 　　DDRR<br /> <b>Sample Output</b><br /> 　　I get there!<br /> 　　I am dizzy!<br /> 　　I have no idea!<br /> 　　I am out!<br /> 　　I get there!<br /> 输出样例: <br />",

            "test_case_id": "3695219681407",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-03-28T03:15:44.272Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 369 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T369",
            "tags": [
                5
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1274,
        "fields": {
            "title": "算法提高 矩阵乘法",
            "description": r"<br />　　有n个矩阵，大小分别为a0*a1, a1*a2, a2*a3, ..., a[n-1]*a[n]，现要将它们依次相乘，只能使用结合率，求最少需要多少次运算。<br /> 　　两个大小分别为p*q和q*r的矩阵相乘时的运算次数计为p*q*r。",
            "input_description": r"输入描述:<br />　　输入的第一行包含一个整数n，表示矩阵的个数。<br /> 　　第二行包含n+1个数，表示给定的矩阵。 <br />输入样例: <br />3<br /> 1 10 5 20",
            "output_description": r"<br />输出描述: <br />　　输出一个整数，表示最少的运算次数。<br /> 输出样例: <br />150",

            "test_case_id": "4175277463858",
            "hint": r"HINT:时间限制：3.0s  内存限制：256.0MB<br />　　1&lt;=n&lt;=1000, 1&lt;=ai&lt;=10000。",
            "create_time": "2018-03-28T03:15:44.275Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 3,
            "source": r"蓝桥杯练习系统 ID: 417 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T417",
            "tags": [
                5
            ]
        }
    },

    {
        "model": "problem.problem",
        "pk": 1025,
        "fields": {
            "title": "历届试题 核桃的数量",
            "description": r"<br /> <p>小张是软件项目经理，他带领3个开发组。工期紧，今天都在加班呢。为鼓舞士气，小张打算给每个组发一袋核桃（据传言能补脑）。他的要求是：</p> <p>1. 各组的核桃数量必须相同</p> <p>2. 各组内必须能平分核桃（当然是不能打碎的）</p> <p>3. 尽量提供满足1,2条件的最小数量（节约闹革命嘛）</p> ",
            "input_description": r"输入描述:<br /> \t输入包含三个正整数a, b, c，表示每个组正在加班的人数，用空格分开（a,b,c&lt;30）   <br />输入样例: <br /> 2 4 5 ",
            "output_description": r"<br />输出描述: <br /> \t输出一个正整数，表示每袋核桃的数量。 <br /> 输出样例: <br /> 20 \t",

            "test_case_id": "24481520425",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.26Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 24 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T24",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1026,
        "fields": {
            "title": "历届试题 打印十字图",
            "description": r"<br /> <p>   小明为某机构设计了一个十字型的徽标（并非红十字会啊），如下所示：</p>  ..$$$$$$$$$$$$$..<br /> ..$...........$..<br /> $$$.$$$$$$$$$.$$$<br /> $...$.......$...$<br /> $.$$$.$$$$$.$$$.$<br /> $.$...$...$...$.$<br /> $.$.$$$.$.$$$.$.$<br /> $.$.$...$...$.$.$<br /> $.$.$.$$$$$.$.$.$<br /> $.$.$...$...$.$.$<br /> $.$.$$$.$.$$$.$.$<br /> $.$...$...$...$.$<br /> $.$$$.$$$$$.$$$.$<br /> $...$.......$...$<br /> $$$.$$$$$$$$$.$$$<br /> ..$...........$..<br /> ..$$$$$$$$$$$$$..  <p>   对方同时也需要在电脑dos窗口中以字符的形式输出该标志，并能任意控制层数。</p> \t",
            "input_description": r"输入描述:<br /> \t一个正整数 n (n&lt;30) 表示要求打印图形的层数。   <br />输入样例: <br /> ..$$$$$$$$$$$$$..<br /> ..$...........$..<br /> $$$.$$$$$$$$$.$$$<br /> $...$.......$...$<br /> $.$$$.$$$$$.$$$.$<br /> $.$...$...$...$.$<br /> $.$.$$$.$.$$$.$.$<br /> $.$.$...$...$.$.$<br /> $.$.$.$$$$$.$.$.$<br /> $.$.$...$...$.$.$<br /> $.$.$$$.$.$$$.$.$<br /> $.$...$...$...$.$<br /> $.$$$.$$$$$.$$$.$<br /> $...$.......$...$<br /> $$$.$$$$$$$$$.$$$<br /> ..$...........$..<br /> ..$$$$$$$$$$$$$.. ",
            "output_description": r"<br />输出描述: <br /> \t对应包围层数的该标志。 <br /> 输出样例: <br /> 1 ",

            "test_case_id": "25500781242",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br /> \t请仔细观察样例，尤其要注意句点的数量和输出位置。 ",
            "create_time": "2018-05-28T03:15:44.27Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 25 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T25",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1027,
        "fields": {
            "title": "历届试题 带分数",
            "description": r"<br /> <p>100 可以表示为带分数的形式：100 = 3 + 69258 / 714。</p> <p>还可以表示为：100 = 82 + 3546 / 197。</p> <p>注意特征：带分数中，数字1~9分别出现且只出现一次（不包含0）。</p> <p>类似这样的带分数，100 有 11 种表示法。</p> \t",
            "input_description": r"输入描述:<br /> <p>从标准输入读入一个正整数N (N&lt;1000*1000)</p>   <br />输入样例: <br /> 100 ",
            "output_description": r"<br />输出描述: <br /> <p>程序输出该数字用数码1~9不重复不遗漏地组成带分数表示的全部种数。</p> <p>注意：不要求输出每个表示，只统计有多少表示法！</p> <br /> 输出样例: <br /> 11 \t",

            "test_case_id": "26520042059",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.28Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 26 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T26",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1028,
        "fields": {
            "title": "历届试题 剪格子",
            "description": r"<br /> <p>如下图所示，3 x 3 的格子中填写了一些整数。</p>  +--*--+--+<br /> |10* 1|52|<br /> +--****--+<br /> |20|30* 1|<br /> *******--+<br /> | 1| 2| 3|<br /> +--+--+--+  <p>我们沿着图中的星号线剪开，得到两个部分，每个部分的数字和都是60。</p>  <p>本题的要求就是请你编程判定：对给定的m x n 的格子中的整数，是否可以分割为两个部分，使得这两个区域的数字和相等。</p> <p>如果存在多种解答，请输出包含左上角格子的那个区域包含的格子的最小数目。   </p> <p>如果无法分割，则输出 0。</p>  \t",
            "input_description": r"输入描述:<br /> \t<p>程序先读入两个整数 m n 用空格分割 (m,n&lt;10)。</p> \t<p>表示表格的宽度和高度。</p> \t<p>接下来是n行，每行m个正整数，用空格分开。每个整数不大于10000。</p>   <br />输入样例: <br /> +--*--+--+<br /> |10* 1|52|<br /> +--****--+<br /> |20|30* 1|<br /> *******--+<br /> | 1| 2| 3|<br /> +--+--+--+ ",
            "output_description": r"<br />输出描述: <br /> 输出一个整数，表示在所有解中，包含左上角的分割区可能包含的最小的格子数目。 <br /> 输出样例: <br /> 3 3<br /> 10 1 52<br /> 20 30 1<br /> 1 2 3 ",

            "test_case_id": "27539302876",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.29Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 27 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T27",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1029,
        "fields": {
            "title": "历届试题 错误票据",
            "description": r"<br /> <p>某涉密单位下发了某种票据，并要在年终全部收回。</p> <p>每张票据有唯一的ID号。全年所有票据的ID号是连续的，但ID的开始数码是随机选定的。</p> <p>因为工作人员疏忽，在录入ID号的时候发生了一处错误，造成了某个ID断号，另外一个ID重号。</p> <p>你的任务是通过编程，找出断号的ID和重号的ID。</p> <p>假设断号不可能发生在最大和最小号。</p> ",
            "input_description": r"输入描述:<br /> <p>要求程序首先输入一个整数N(N&lt;100)表示后面数据行数。</p> <p>接着读入N行数据。</p> <p>每行数据长度不等，是用空格分开的若干个（不大于100个）正整数（不大于100000），请注意行内和行末可能有多余的空格，你的程序需要能处理这些空格。</p> <p>每个整数代表一个ID号。</p>  <br />输入样例: <br />2<br /> 5 6 8 11 9 <br /> 10 12 9",
            "output_description": r"<br />输出描述: <br /> <p>要求程序输出1行，含两个整数m n，用空格分隔。</p> <p>其中，m表示断号ID，n表示重号ID</p> <br /> 输出样例: <br />7 9",

            "test_case_id": "28558563693",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.30Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 28 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T28",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1030,
        "fields": {
            "title": "历届试题 翻硬币",
            "description": r"<br />  <p>小明正在玩一个“翻硬币”的游戏。</p> <p>桌上放着排成一排的若干硬币。我们用 * 表示正面，用 o 表示反面（是小写字母，不是零）。</p> <p>比如，可能情形是：**oo***oooo</p>  <p>如果同时翻转左边的两个硬币，则变为：oooo***oooo</p> <p>现在小明的问题是：如果已知了初始状态和要达到的目标状态，每次只能同时翻转相邻的两个硬币,那么对特定的局面，最少要翻动多少次呢？</p> <p>我们约定：把翻动相邻的两个硬币叫做一步操作，那么要求：  ",
            "input_description": r"输入描述:<br />  <p>两行等长的字符串，分别表示初始状态和要达到的目标状态。每行的长度<1000</p>   <br />输入样例: <br /> **********<br /> o****o****<br /> ",
            "output_description": r"<br />输出描述: <br />  <p>一个整数，表示最小操作步数。</p>  <br /> 输出样例: <br /> 5 \t",

            "test_case_id": "29577824510",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.31Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 29 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T29",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1031,
        "fields": {
            "title": "历届试题 连号区间数",
            "description": r"<br />  <p>小明这些天一直在思考这样一个奇怪而有趣的问题：</p> <p>在1~N的某个全排列中有多少个连号区间呢？这里所说的连号区间的定义是：</p> <p>如果区间[L, R] 里的所有元素（即此排列的第L个到第R个元素）递增排序后能得到一个长度为R-L+1的“连续”数列，则称这个区间连号区间。</p> <p>当N很小的时候，小明可以很快地算出答案，但是当N变大的时候，问题就不是那么简单了，现在小明需要你的帮助。</p>  ",
            "input_description": r"输入描述:<br />  <p>第一行是一个正整数N (1 <= N <= 50000), 表示全排列的规模。</p> <p>第二行是N个不同的数字Pi(1 <= Pi <= N)， 表示这N个数字的某一全排列。</p>   <br />输入样例: <br /> 4<br/> 3 2 4 1<br /> ",
            "output_description": r"<br />输出描述: <br />  <p>输出一个整数，表示不同连号区间的数目。</p>  <br /> 输出样例: <br /> 7 \t",

            "test_case_id": "30597085327",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.32Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 30 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T30",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1032,
        "fields": {
            "title": "历届试题 买不到的数目",
            "description": r"<br />  <p>小明开了一家糖果店。他别出心裁：把水果糖包成4颗一包和7颗一包的两种。糖果不能拆包卖。</p> <p>小朋友来买糖的时候，他就用这两种包装来组合。当然有些糖果数目是无法组合出来的，比如要买 10 颗糖。</p> <p>你可以用计算机测试一下，在这种包装情况下，最大不能买到的数量是17。大于17的任何数字都可以用4和7组合出来。</p> <p>本题的要求就是在已知两个包装的数量时，求最大不能组合出的数字。</p>  ",
            "input_description": r"输入描述:<br />  <p>两个正整数，表示每种包装中糖的颗数(都不多于1000)</p>   <br />输入样例: <br /> 4 7<br/> ",
            "output_description": r"<br />输出描述: <br />  <p>一个正整数，表示最大不能买到的糖数</p>  <br /> 输出样例: <br /> 17 \t",

            "test_case_id": "31616346144",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.33Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 31 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T31",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1033,
        "fields": {
            "title": "历届试题 大臣的旅费",
            "description": r"<br />  <p>很久以前，T王国空前繁荣。为了更好地管理国家，王国修建了大量的快速路，用于连接首都和王国内的各大城市。</p> <p>为节省经费，T国的大臣们经过思考，制定了一套优秀的修建方案，使得任何一个大城市都能从首都直接或者通过其他大城市间接到达。同时，如果不重复经过大城市，从首都到达每个大城市的方案都是唯一的。</p> <p>J是T国重要大臣，他巡查于各大城市之间，体察民情。所以，从一个城市马不停蹄地到另一个城市成了J最常做的事情。他有一个钱袋，用于存放往来城市间的路费。</p> <p>聪明的J发现，如果不在某个城市停下来修整，在连续行进过程中，他所花的路费与他已走过的距离有关，在走第x千米到第x+1千米这一千米中（x是整数），他花费的路费是x+10这么多。也就是说走1千米花费11，走2千米要花费23。</p> <p>J大臣想知道：他从某一个城市出发，中间不休息，到达另一个城市，所有可能花费的路费中最多是多少呢？</p>  ",
            "input_description": r"输入描述:<br />  <p>输入的第一行包含一个整数n，表示包括首都在内的T王国的城市数</p> <p>城市从1开始依次编号，1号城市为首都。</p> <p>接下来n-1行，描述T国的高速路（T国的高速路一定是n-1条）</p> <p>每行三个整数Pi, Qi, Di，表示城市Pi和城市Qi之间有一条高速路，长度为Di千米。</p>   <br />输入样例: <br /> 5<br/> 1 2 2<br /> 1 3 1<br /> 2 4 5<br /> 2 5 4<br/> ",
            "output_description": r"<br />输出描述: <br />  <p>输出一个整数，表示大臣J最多花费的路费是多少。</p>  <br /> 输出样例: <br /> 135 \t",

            "test_case_id": "32635606961",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />  <p>大臣J从城市4到城市5要花费135的路费。</p>  ",
            "create_time": "2018-05-28T03:15:44.34Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 32 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T32",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1034,
        "fields": {
            "title": "历届试题 幸运数",
            "description": r"<br />  <p>    幸运数是波兰数学家乌拉姆命名的。它采用与生成素数类似的“筛法”生成</p>。 <p>    首先从1开始写出自然数1,2,3,4,5,6,....</p> <p>    1 就是第一个幸运数。</p> <p>    我们从2这个数开始。把所有序号能被2整除的项删除，变为：</p> <p>    1 _ 3 _ 5 _ 7 _ 9 ....</p> <p>    把它们缩紧，重新记序，为：</p>  <p>   1 3 5 7 9 .... 。这时，3为第2个幸运数，然后把所有能被3整除的序号位置的数删去。注意，是序号位置，不是那个数本身能否被3整除!! 删除的应该是5，11, 17, ...</p> <p>    此时7为第3个幸运数，然后再删去序号位置能被7整除的(19,39,...)</p>   <p>   最后剩下的序列类似：</p> <p>    1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, ...</p>  ",
            "input_description": r"输入描述:<br />  输入两个正整数m n, 用空格分开 (m &lt; n &lt; 1000*1000)   <br />输入样例: <br /> 1 20 ",
            "output_description": r"<br />输出描述: <br />  程序输出 位于m和n之间的幸运数的个数（不包含m和n）。  <br /> 输出样例: <br /> 5 \t",

            "test_case_id": "33654867778",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.35Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 33 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T33",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1035,
        "fields": {
            "title": "历届试题 横向打印二叉树",
            "description": r"<br />  <p>二叉树可以用于排序。其原理很简单：对于一个排序二叉树添加新节点时，先与根节点比较，若小则交给左子树继续处理，否则交给右子树。</p> <p>当遇到空子树时，则把该节点放入那个位置。 </p> <p>比如，10 8 5 7 12 4 的输入顺序，应该建成二叉树如下图所示，其中.表示空白。</p>   ...|-12<br /> 10-|<br /> ...|-8-|<br /> .......|...|-7<br /> .......|-5-|<br /> ...........|-4  <p>本题目要求：根据已知的数字，建立排序二叉树，并在标准输出中横向打印该二叉树。 </p>  ",
            "input_description": r"输入描述:<br />  <p>输入数据为一行空格分开的N个整数。 N&lt;100，每个数字不超过10000。</p> <p>输入数据中没有重复的数字。 </p>   <br />输入样例: <br /> ...|-12<br /> 10-|<br /> ...|-8-|<br /> .......|...|-7<br /> .......|-5-|<br /> ...........|-4 ",
            "output_description": r"<br />输出描述: <br />  <p>输出该排序二叉树的横向表示。为了便于评卷程序比对空格的数目，请把空格用句点代替：</p>  <br /> 输出样例: <br /> 10 5 20 ",

            "test_case_id": "34674128595",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.36Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 34 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T34",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1036,
        "fields": {
            "title": "历届试题 危险系数",
            "description": r"<br />  <p>抗日战争时期，冀中平原的地道战曾发挥重要作用。</p> <p>地道的多个站点间有通道连接，形成了庞大的网络。但也有隐患，当敌人发现了某个站点后，其它站点间可能因此会失去联系。</p> <p>我们来定义一个危险系数DF(x,y)：</p> <p>对于两个站点x和y (x != y), 如果能找到一个站点z，当z被敌人破坏后，x和y不连通，那么我们称z为关于x,y的关键点。相应的，对于任意一对站点x和y，危险系数DF(x,y)就表示为这两点之间的关键点个数。</p> <p>本题的任务是：已知网络结构，求两站点之间的危险系数。</p>  ",
            "input_description": r"输入描述:<br />  <p>输入数据第一行包含2个整数n(2 &lt;= n &lt;= 1000), m(0 &lt;= m &lt;= 2000),分别代表站点数，通道数；</p> <p>接下来m行，每行两个整数 u,v (1 &lt;= u, v &lt;= n; u != v)代表一条通道；</p> <p>最后1行，两个数u,v，代表询问两点之间的危险系数DF(u, v)。</p>   <br />输入样例: <br /> 7 6<br /> 1 3<br /> 2 3<br /> 3 4<br /> 3 5<br /> 4 5<br /> 5 6<br /> 1 6  ",
            "output_description": r"<br />输出描述: <br />  一个整数，如果询问的两点不连通则输出-1.  <br /> 输出样例: <br /> 2 \t",

            "test_case_id": "35693389412",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.37Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 35 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T35",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1037,
        "fields": {
            "title": "历届试题 网络寻路",
            "description": r"<br />  <p>X 国的一个网络使用若干条线路连接若干个节点。节点间的通信是双向的。某重要数据包，为了安全起见，必须恰好被转发两次到达目的地。该包可能在任意一个节点产生，我们需要知道该网络中一共有多少种不同的转发路径。</p> <p>源地址和目标地址可以相同，但中间节点必须不同。</p> <p>如下图所示的网络。</p> <p><img src=\"/RequireFile.do?fid=JBf444aT\" width=\"502\" height=\"376\" alt=\"\" /></p> <p>1 -&gt; 2 -&gt; 3 -&gt; 1  是允许的</p> <p>1 -&gt; 2 -&gt; 1 -&gt; 2 或者 1 -&gt; 2 -&gt; 3 -&gt; 2 都是非法的。</p>  ",
            "input_description": r"输入描述:<br />  <p>输入数据的第一行为两个整数N M，分别表示节点个数和连接线路的条数(1&lt;=N&lt;=10000; 0&lt;=M&lt;=100000)。</p> <p>接下去有M行，每行为两个整数 u 和 v，表示节点u 和 v 联通(1&lt;=u,v&lt;=N , u!=v)。</p> <p>输入数据保证任意两点最多只有一条边连接，并且没有自己连自己的边，即不存在重边和自环。</p>   <br />输入样例: <br /> 3 3<br /> 1 2<br /> 2 3<br /> 1 3 ",
            "output_description": r"<br />输出描述: <br />      输出一个整数，表示满足要求的路径条数。  <br /> 输出样例: <br /> 6 \t",

            "test_case_id": "36712650229",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.38Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 36 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T36",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1038,
        "fields": {
            "title": "历届试题 高僧斗法",
            "description": r"<br />　　古时丧葬活动中经常请高僧做法事。仪式结束后，有时会有“高僧斗法”的趣味节目，以舒缓压抑的气氛。<br /> 　　节目大略步骤为：先用粮食（一般是稻米）在地上“画”出若干级台阶（表示N级浮屠）。又有若干小和尚随机地“站”在某个台阶上。最高一级台阶必须站人，其它任意。(如图1所示)<br /> 　　两位参加游戏的法师分别指挥某个小和尚向上走任意多级的台阶，但会被站在高级台阶上的小和尚阻挡，不能越过。两个小和尚也不能站在同一台阶，也不能向低级台阶移动。<br /> 　　两法师轮流发出指令，最后所有小和尚必然会都挤在高段台阶，再也不能向上移动。轮到哪个法师指挥时无法继续移动，则游戏结束，该法师认输。<br /> 　　对于已知的台阶数和小和尚的分布位置，请你计算先发指令的法师该如何决策才能保证胜出。",
            "input_description": r"输入描述:<br />　　输入数据为一行用空格分开的N个整数，表示小和尚的位置。台阶序号从1算起，所以最后一个小和尚的位置即是台阶的总数。（N&lt;100, 台阶总数&lt;1000） <br />输入样例: <br />1 5 9",
            "output_description": r"<br />输出描述: <br />　　输出为一行用空格分开的两个整数: A B, 表示把A位置的小和尚移动到B位置。若有多个解，输出A值较小的解，若无解则输出-1。<br /> 输出样例: <br />1 4",

            "test_case_id": "37731911046",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.39Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 37 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T37",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1039,
        "fields": {
            "title": "历届试题 格子刷油漆",
            "description": r"<br />　　X国的一段古城墙的顶端可以看成 2*N个格子组成的矩形（如下图所示），现需要把这些格子刷上保护漆。<br /> <br /> <img src=\"/RequireFile.do?fid=HLt96rLF\" width=\"439\" height=\"234\" /><br /> 　　你可以从任意一个格子刷起，刷完一格，可以移动到和它相邻的格子（对角相邻也算数），但不能移动到较远的格子（因为油漆未干不能踩！）<br /> 　　比如：a d b c e f 就是合格的刷漆顺序。<br /> 　　c e f d a b 是另一种合适的方案。<br /> 　　当已知 N 时，求总的方案数。当N较大时，结果会迅速增大，请把结果对 1000000007 (十亿零七) 取模。",
            "input_description": r"输入描述:<br />　　输入数据为一个正整数（不大于1000） <br />输入样例: <br />2",
            "output_description": r"<br />输出描述: <br />　　输出数据为一个正整数。<br /> 输出样例: <br />24",

            "test_case_id": "38751171863",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.40Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 38 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T38",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1040,
        "fields": {
            "title": "历届试题 农场阳光",
            "description": r"<br />　　X星球十分特殊，它的自转速度与公转速度相同，所以阳光总是以固定的角度照射。<br /> 　　最近，X星球为发展星际旅游业，把空间位置出租给Y国游客来晒太阳。每个租位是漂浮在空中的圆盘形彩云（圆盘与地面平行）。当然，这会遮挡住部分阳光，被遮挡的土地植物无法生长。<br /> 　　本题的任务是计算某个农场宜于作物生长的土地面积有多大。",
            "input_description": r"输入描述:<br />　　输入数据的第一行包含两个整数a, b，表示某农场的长和宽分别是a和b，此时，该农场的范围是由坐标(0, 0, 0), (a, 0, 0), (a, b, 0), (0, b, 0)围成的矩形区域。<br /> 　　第二行包含一个实数g，表示阳光照射的角度。简单起见，我们假设阳光光线是垂直于农场的宽的，此时正好和农场的长的夹角是g度，此时，空间中的一点(x, y, z)在地面的投影点应该是(x + z * ctg(g度), y, 0)，其中ctg(g度)表示g度对应的余切值。<br /> 　　第三行包含一个非负整数n，表示空中租位个数。<br /> 　　接下来 n 行，描述每个租位。其中第i行包含4个整数xi, yi, zi, ri，表示第i个租位彩云的圆心在(xi, yi, zi)位置，圆半径为ri。 <br />输入样例: <br />10 10<br /> 90.0<br /> 1<br /> 5 5 10 5",
            "output_description": r"<br />输出描述: <br />　　要求输出一个实数，四舍五入保留两位有效数字，表示农场里能长庄稼的土地的面积。<br /> 输出样例: <br />21.46",

            "test_case_id": "39770432680",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.41Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 39 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T39",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1041,
        "fields": {
            "title": "历届试题 约数倍数选卡片",
            "description": r"<br />　　闲暇时，福尔摩斯和华生玩一个游戏：<br /> 　　在N张卡片上写有N个整数。两人轮流拿走一张卡片。要求下一个人拿的数字一定是前一个人拿的数字的约数或倍数。例如，某次福尔摩斯拿走的卡片上写着数字“6”，则接下来华生可以拿的数字包括：<br /> 　　1，2，3, 6，12，18，24 ....<br /> 　　当轮到某一方拿卡片时，没有满足要求的卡片可选，则该方为输方。<br /> 　　请你利用计算机的优势计算一下，在已知所有卡片上的数字和可选哪些数字的条件下，怎样选择才能保证必胜！<br /> 　　当选多个数字都可以必胜时，输出其中最小的数字。如果无论如何都会输，则输出-1。",
            "input_description": r"输入描述:<br />　　输入数据为2行。第一行是若干空格分开的整数（每个整数介于1~100间），表示当前剩余的所有卡片。<br /> 　　第二行也是若干空格分开的整数，表示可以选的数字。当然，第二行的数字必须完全包含在第一行的数字中。 <br />输入样例: <br />2 3 6<br /> 3 6",
            "output_description": r"<br />输出描述: <br />　　程序则输出必胜的招法！！<br /> 输出样例: <br />3",

            "test_case_id": "40789693497",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.42Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 40 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T40",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1042,
        "fields": {
            "title": "历届试题 车轮轴迹",
            "description": r"<br />　　栋栋每天骑自行车回家需要经过一条狭长的林荫道。道路由于年久失修，变得非常不平整。虽然栋栋每次都很颠簸，但他仍把骑车经过林荫道当成一种乐趣。<br /> 　　由于颠簸，栋栋骑车回家的路径是一条上下起伏的曲线，栋栋想知道，他回家的这条曲线的长度究竟是多长呢？更准确的，栋栋想知道从林荫道的起点到林荫道的终点，他的车前轮的轴（圆心）经过的路径的长度。<br /> 　　栋栋对路面进行了测量。他把道路简化成一条条长短不等的直线段，这些直线段首尾相连，且位于同一平面内。并在该平面内建立了一个直角坐标系，把所有线段的端点坐标都计算好。<br /> 　　假设栋栋的自行车在行进的过程中前轮一直是贴着路面前进的。<br /> <br /> <img src=\"/RequireFile.do?fid=tAMBefqe\" width=\"512\" height=\"256\" /><br /> 　　上图给出了一个简单的路面的例子，其中蓝色实线为路面，红色虚线为车轮轴经过的路径。在这个例子中，栋栋的前轮轴从A点出发，水平走到B点，然后绕着地面的F点到C点（绕出一个圆弧），再沿直线下坡到D点，最后水平走到E点，在这个图中地面的坐标依次为：(0, 0), (2, 0), (4, -1), (6, -1)，前轮半径为1.50，前轮轴前进的距离依次为：<br /> 　　AB=2.0000；弧长BC=0.6955；CD=1.8820；DE=1.6459。<br /> 　　总长度为6.2233。<br /> <br /> 　　下图给出了一个较为复杂的路面的例子，在这个例子中，车轮在第一个下坡还没下完时（D点）就开始上坡了，之后在坡的顶点要从E绕一个较大的圆弧到F点。这个图中前轮的半径为1，每一段的长度依次为：<br /> 　　AB=3.0000；弧长BC=0.9828；CD=1.1913；DE=2.6848；弧长EF=2.6224；    FG=2.4415；GH=2.2792。<br /> 　　总长度为15.2021。<br /> <img src=\"/RequireFile.do?fid=jQtyey68\" width=\"680\" height=\"400\" /><br /> 　　现在给出了车轮的半径和路面的描述，请求出车轮轴轨迹的总长度。",
            "input_description": r"输入描述:<br />　　输入的第一行包含一个整数n和一个实数r，用一个空格分隔，表示描述路面的坐标点数和车轮的半径。<br /> 　　接下来n行，每个包含两个实数，其中第i行的两个实数x[i], y[i]表示描述路面的第i个点的坐标。<br /> 　　路面定义为所有路面坐标点顺次连接起来的折线。给定的路面的一定满足以下性质：<br /> <br /> 　　*第一个坐标点一定是(0, 0)；<br /> 　　*第一个点和第二个点的纵坐标相同；<br /> 　　*倒数第一个点和倒数第二个点的纵坐标相同；<br /> 　　*第一个点和第二个点的距离不少于车轮半径；<br /> 　　*倒数第一个点和倒数第二个点的的距离不少于车轮半径；<br /> 　　*后一个坐标点的横坐标大于前一个坐标点的横坐标，即对于所有的i，x[i+1]&gt;x[i]。 <br />输入样例: <br />4 1.50<br /> 0.00 0.00<br /> 2.00 0.00<br /> 4.00 -1.00<br /> 6.00 -1.00",
            "output_description": r"<br />输出描述: <br />　　输出一个实数，四舍五入保留两个小数，表示车轮轴经过的总长度。<br /> 　　你的结果必须和参考答案一模一样才能得分。数据保证答案精确值的小数点后第三位不是4或5。<br /> 输出样例: <br />6.22",

            "test_case_id": "41808954314",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　这个样例对应第一个图。",
            "create_time": "2018-05-28T03:15:44.43Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 41 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T41",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1043,
        "fields": {
            "title": "历届试题 九宫重排",
            "description": r"<br />　　如下面第一个图的九宫格中，放着 1~8 的数字卡片，还有一个格子空着。与空格子相邻的格子中的卡片可以移动到空格中。经过若干次移动，可以形成第二个图所示的局面。<br /> <img src=\"/RequireFile.do?fid=qYebaGed\" width=\"236\" height=\"245\" /><img src=\"/RequireFile.do?fid=HQ3JFM72\" width=\"236\" height=\"245\" /><br /> 　　我们把第一个图的局面记为：12345678.<br /> 　　把第二个图的局面记为：123.46758<br /> 　　显然是按从上到下，从左到右的顺序记录数字，空格记为句点。<br /> 　　本题目的任务是已知九宫的初态和终态，求最少经过多少步的移动可以到达。如果无论多少步都无法到达，则输出-1。",
            "input_description": r"输入描述:<br />　　输入第一行包含九宫的初态，第二行包含九宫的终态。 <br />输入样例: <br />12345678.<br /> 123.46758",
            "output_description": r"<br />输出描述: <br />　　输出最少的步数，如果不存在方案，则输出-1。<br /> 输出样例: <br />3",

            "test_case_id": "42828215131",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />",
            "create_time": "2018-05-28T03:15:44.44Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 42 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T42",
            "tags": [
                6
            ]
        }
    },
    {
        "model": "problem.problem",
        "pk": 1044,
        "fields": {
            "title": "历届试题 公式求值",
            "description": r"<br />　　输入n, m, k，输出下面公式的值。<br /> <img src=\"/RequireFile.do?fid=FJ9YqBGE\" width=\"317\" height=\"129\" /><br /> 　　其中C_n^m是组合数，表示在n个人的集合中选出m个人组成一个集合的方案数。组合数的计算公式如下。<br /> <img src=\"/RequireFile.do?fid=TEm3EGfy\" width=\"1160\" height=\"112\" />",
            "input_description": r"输入描述:<br />　　输入的第一行包含一个整数n；第二行包含一个整数m，第三行包含一个整数k。 <br />输入样例: <br />3<br /> 1<br /> 3",
            "output_description": r"<br />输出描述: <br />　　计算上面公式的值，由于答案非常大，请输出这个值除以999101的余数。<br /> 输出样例: <br />162",

            "test_case_id": "43847475948",
            "hint": r"HINT:时间限制：1.0s  内存限制：256.0MB<br />　　对于10%的数据，n≤10，k≤3；<br /> 　　对于20%的数据，n≤20，k≤3；<br /> 　　对于30%的数据，n≤1000，k≤5；<br /> 　　对于40%的数据，n≤10^7，k≤10；<br /> 　　对于60%的数据，n≤10^15，k ≤100；<br /> 　　对于70%的数据，n≤10^100，k≤200；<br /> 　　对于80%的数据，n≤10^500，k ≤500；<br /> 　　对于100%的数据，n在十进制下不超过1000位，即1≤n&lt;10^1000，1≤k≤1000，同时0≤m≤n，k≤n。",
            "create_time": "2018-05-28T03:15:44.45Z",
            "last_update_time": "null",
            "created_by": 1,
            "time_limit": 1000,
            "memory_limit": 512,
            "spj": "false",
            "spj_language": "null",
            "spj_code": "null",
            "spj_version": "null",
            "visible": "true",
            "total_submit_number": 0,
            "total_accepted_number": 0,
            "difficulty": 2,
            "source": r"蓝桥杯练习系统 ID: 43 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T43",
            "tags": [
                6
            ]
        }
    }

]

import os
import shutil

os.mkdir("json")

cnt = 0

num = 1240
while True:
    path = "test_case\\"
    os.mkdir("json\\" + str(cnt + 1))
    json_dict = {
        "display_id": "",
        "title": "",
        "description": {
            "format": "html",
            "value": ""
        },
        "tags": [
            "FATE"
        ],
        "input_description": {
            "format": "html",
            "value": ""
        },
        "output_description": {
            "format": "html",
            "value": ""
        },
        "test_case_score": [],
        "hint": {
            "format": "html",
            "value": ""
        },
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": [
            {
                "input": "",
                "output": ""
            }
        ],
        "template": {},
        "spj": "null",
        "rule_type": "ACM",
        "source": "来源",
        "answers": []
    }
    test_path = path + dict[cnt]["fields"]["test_case_id"]
    sorce = 100 // (len(os.listdir(test_path)) // 2)
    cnt1 = 1
    cnt2 = 1
    for i in range(0, len(os.listdir(test_path)) // 2):

        if i != 0:
            json_dict["test_case_score"].append(
                ',{' + '"score": {},"input_name": "{}.in","output_name": "{}.out"'.format(sorce, cnt1,
                                                                                          cnt2) + '}')
        else:
            json_dict["test_case_score"].append(
                '{' + '"score": {},"input_name": "{}.in","output_name": "{}.out"'.format(sorce, cnt1,
                                                                                         cnt2) + '}')

        cnt1 += 1
        cnt2 += 1

    shutil.move(test_path, "json\\" + str(cnt + 1))
    os.rename("json\\" + str(cnt + 1) + "\\" + dict[cnt]["fields"]["test_case_id"],
              "json\\" + str(cnt + 1) + "\\" + "testcase")
    json_dict["display_id"] = num
    json_dict["title"] = dict[cnt]["fields"]["title"]
    json_dict["description"]["value"] = dict[cnt]["fields"]["description"]
    json_dict["input_description"]["value"] = dict[cnt]["fields"]["input_description"]
    json_dict["output_description"]["value"] = dict[cnt]["fields"]["output_description"]
    json_dict["hint"]["value"] = dict[cnt]["fields"]["hint"]

    json_dict["samples"][0]["input"] = "题意"
    json_dict["samples"][0]["output"] = "题意"
    json_dict["source"] = "FATE_YO"

    json_data = json.dumps(json_dict, indent=4)

    # 将JSON格式的文本写入文件

    path = "json\\" + str(cnt + 1) + '\\'
    with open(path + "problem.json", 'w') as f:
        f.write(json_data)
    num += 1
    cnt += 1
