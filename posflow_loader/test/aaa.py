# 打开一个文件
fo = open("/home/zeppelin/test_data/bank.csv", "w")
print("文件名: " + fo.name)

data = """
"age";"job";"marital";"education";"default";"balance";"housing";"loan";"contact";"day";"month";"duration";"campaign";"pdays";"previous";"poutcome";"y"
30;"unemployed";"married";"primary";"no";1787;"no";"no";"cellular";19;"oct";79;1;-1;0;"unknown";"no"
33;"services";"married";"secondary";"no";4789;"yes";"yes";"cellular";11;"may";220;1;339;4;"failure";"no"
35;"management";"single";"tertiary";"no";1350;"yes";"no";"cellular";16;"apr";185;1;330;1;"failure";"no"
30;"management";"married";"tertiary";"no";1476;"yes";"yes";"unknown";3;"jun";199;4;-1;0;"unknown";"no"
59;"blue-collar";"married";"secondary";"no";0;"yes";"no";"unknown";5;"may";226;1;-1;0;"unknown";"no"
35;"management";"single";"tertiary";"no";747;"no";"no";"cellular";23;"feb";141;2;176;3;"failure";"no"
36;"self-employed";"married";"tertiary";"no";307;"yes";"no";"cellular";14;"may";341;1;330;2;"other";"no"
39;"technician";"married";"secondary";"no";147;"yes";"no";"cellular";6;"may";151;2;-1;0;"unknown";"no"
41;"entrepreneur";"married";"tertiary";"no";221;"yes";"no";"unknown";14;"may";57;2;-1;0;"unknown";"no"
43;"services";"married";"primary";"no";-88;"yes";"yes";"cellular";17;"apr";313;1;147;2;"failure";"no"
39;"services";"married";"secondary";"no";9374;"yes";"no";"unknown";20;"may";273;1;-1;0;"unknown";"no"
43;"admin.";"married";"secondary";"no";264;"yes";"no";"cellular";17;"apr";113;2;-1;0;"unknown";"no"
36;"technician";"married";"tertiary";"no";1109;"no";"no";"cellular";13;"aug";328;2;-1;0;"unknown";"no"
20;"student";"single";"secondary";"no";502;"no";"no";"cellular";30;"apr";261;1;-1;0;"unknown";"yes"
31;"blue-collar";"married";"secondary";"no";360;"yes";"yes";"cellular";29;"jan";89;1;241;1;"failure";"no"
40;"management";"married";"tertiary";"no";194;"no";"yes";"cellular";29;"aug";189;2;-1;0;"unknown";"no"
"""
fo.write( data)
# 关闭打开的文件
fo.close()
