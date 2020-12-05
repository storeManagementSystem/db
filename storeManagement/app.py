from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# 访问主页，返回主页的html文件
@app.route("/")
def home():
    return render_template("sell.html")

####################销售模块

# sell销售功能模块:查询顾客总积分数、检查顾客号是否存在（前端填写会员编号，点击确认按钮时触发）
# 前端发送 1.顾客编号cno            获取方法：cno=request.get_json()['cno']
# 后端：若顾客存在返回总积分数，不存在...
@app.route("/queryCustomer",methods=['POST', 'GET'])
def query_customer():
    if request.method == 'POST':
        cno=request.get_json()['cno']
        if cno != '':
            return jsonify(100)
        else:
            return jsonify('Failed')

# sell销售功能模块：输入商品编号，点击增加按钮时触发
# 前端发送gno
# 后端返回该商品的相关信息
@app.route("/sell",methods=['POST', 'GET'])
def sell():
    a="伊利牛奶"
    add_good = {
            "gno": "G18970",
            "gname": a,
            "outprice": 3,
            "amount":1,
        }

    if request.method == 'POST':
        gno=request.get_json()['gno']
        if gno != '':
            return jsonify(add_good)
    elif request.method == 'GET':
        return render_template("sell.html")

# sell销售功能模块: 查询顾客可用的积分数（前端点击提交订单按钮时触发）
# 前端发送 1.顾客编号cno，2.顾客购买的商品数组good_list
# 后端返回检查用户是否存在，根据一定规则计算，返回相应的可用积分数
@app.route("/queryPoints",methods=['POST', 'GET'])
def query_point():
    if request.method == 'POST':
        cno=request.get_json()['cno']
        good_list=request.get_json()['good_list']
        if cno != '':
            return jsonify(500)
        else:
            return jsonify('Failed')

# sell销售功能模块：提交售卖订单（前端填写使用积分数，并提交时触发）
# 前端向服务器发送 1.商品数组good_list 2. 使用积分数pointsUsed，后端发送提交成功/失败
@app.route("/submitOrder",methods=['POST', 'GET'])
def submit_order():
    if request.method == 'POST':
        ponitsUsed = request.get_json()['pointsUsed']
        good_list = request.get_json()['good_list']
        if ponitsUsed != 0:
            return jsonify('提交成功')
        else:
            return jsonify('提交失败')


####################进货模块

# purchase进货功能模块：访问进货页面时触发
# 后端：返回所有进货订单的数组
@app.route('/api/purchase_all')
def index():
    my_list = [
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"已完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "未完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"未完成"
        },  {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"已完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "未完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"未完成"
        },  {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"已完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "未完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"未完成"
        },  {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"已完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "未完成"
        },
        {
            "pno": "D10830155",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state":"未完成"
        }
    ]
    return jsonify(my_list)

# purchase进货功能模块：根据订单编号/进货商编号/订单状态/进货商编号+订单状态查询相关订单信息 （点击查询按钮时触发）
# 前端发送pno,suno,state          eg. pno:'D123' , suno:'' , state:'' / pno:'' , suno:'S2213' , state:'未完成'
# 后端返回符合该条件订单的相关信息
@app.route("/purchase",methods=['POST', 'GET'])
def purchase():
    my_list1 = [
        {
            "pno": "D1",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "已完成"
        }]
    my_list2 = [
        {
            "pno": "D2",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "已完成"
        }]
    my_list3 = [
        {
            "pno": "D3",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "已完成"
        }]
    my_list4 = [
        {
            "pno": "D4",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "已完成"
        }]
    my_list5 = [
        {
            "pno": "D5",
            "suno": "S23317790",
            "sno": "Y1187",
            "setup_date": "2020.11.30",
            "p_date": "---",
            "pgamt": 5678,
            "state": "已完成"
        }]
    if request.method == 'POST':
        pno=request.get_json()['pno']
        suno=request.get_json()['suno']
        state=request.get_json()['state']
        if pno != '':
            return jsonify(my_list1)
        elif suno != '' and state != '':
            return jsonify(my_list2)
        elif suno !='':
            return jsonify(my_list3)
        elif state != '':
            return jsonify(my_list4)
        else:
            return jsonify(my_list5)
    elif request.method == 'GET':
        return render_template("purchase.html")

@app.route("/add_detail",methods=['POST', 'GET'])
def addDetail():
    a = "伊利牛奶"
    add_good = {
        "gno": "G18970",
        "gname": a,
        "inprice": 2,
        "amount": 1,
    }
    if request.method == 'POST':
        print(request.get_json()['gno']!='')
        return jsonify(add_good)


# purchase进货模块：未完成的进货订单被修改
# 前端向服务器发送 1.进货订单号 pno 2.修改后的全部商品数组 good_list（该订单中的所有商品）
# 后端根据该数组修改数据库相关信息,并返回相关信息
# 进货订单号: request.get_json()['pno'], 修改后的【全部】商品数组: request.get_json()['good_list']
@app.route("/change_detail",methods=['POST', 'GET'])
def changeDetail():
    if request.method == 'POST':
        print(request.get_json())
        return jsonify("修改成功")

# purchase进货模块：查询某一进货订单的商品详情
# 前端向服务器发送 1.进货订单号pno
# 后端发送该订单号含有的 1.商品数组
@app.route("/purchase_detail",methods=['POST', 'GET'])
def purchaseDetail():
    good_list= [
                   {
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 50
                   },
                   {
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 20
                   },
                   {
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 10
                   },{
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 10
                   },{
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 10
                   },{
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 10
                   },{
                       "gno": "G18970",
                       "gname": "伊利牛奶",
                       "inprice": 2,
                       "amount": 10
                   }
               ]
    if request.method == 'POST':
        return jsonify(good_list)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
