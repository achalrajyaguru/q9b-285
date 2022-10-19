from datetime import datetime
import yfinance as yf
from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        
        now = datetime.now()

        symbol1 = request.form.get("symbol1")
        user_input1= round(float(request.form.get("user_input1")),2)
        companyInfo1 = yf.Ticker(symbol1)

        symbol2 = request.form.get("symbol2")
        user_input2= round(float(request.form.get("user_input2")),2)
        companyInfo2 = yf.Ticker(symbol2)

        symbol3 = request.form.get("symbol3")
        user_input3= round(float(request.form.get("user_input3")),2)
        companyInfo3 = yf.Ticker(symbol3)

        symbol4 = request.form.get("symbol4")
        user_input4= round(float(request.form.get("user_input4")),2)
        companyInfo4 = yf.Ticker(symbol4)

        symbol5 = request.form.get("symbol5")
        user_input5= round(float(request.form.get("user_input5")),2)
        companyInfo5 = yf.Ticker(symbol5)

        symbol = [symbol1, symbol2, symbol3, symbol4, symbol5]

        user_input = [user_input1, user_input2, user_input3, user_input4, user_input5]

        companyInfo = [companyInfo1, companyInfo2, companyInfo3, companyInfo4, companyInfo5]
        
        tempData = {}


        for i in companyInfo:
            if i.history(period="max").empty:
                tempData = {"error":"You have entered wrong symbol"}
                return render_template("index.html", **tempData)
        
        
        tempData['error'] = ''
        

        for i in range(0, 5):
            
            companyName=companyInfo[i].info['longName']
            twoDaysData = round(companyInfo[i].history(period='2d'),2)
            yesterdayPrice=twoDaysData['Close'][0]
            todaysPrice=twoDaysData['Close'][1]
            valueChange=round(todaysPrice-user_input[i],2)
            percentChange=round((valueChange/user_input[i])*100,2)


            tempData["now"+str(i)]=now
            tempData["companyName"+str(i)]=companyName
            tempData["user_input"+str(i)]=user_input[i]
            tempData["twoDaysData"+str(i)]=twoDaysData['Close'][1]
            tempData["valueChange"+str(i)]=valueChange
            tempData["percentChange"+str(i)]=percentChange


    
        return render_template("index.html", **tempData)









      

        if companyInfo.history(period="max").empty is False:

            companyName=companyInfo.info['longName']
            twoDaysData = round(companyInfo.history(period='2d'),2)
            yesterdayPrice=twoDaysData['Close'][0]
            todaysPrice=twoDaysData['Close'][1]
            valueChange=round(todaysPrice-user_input,2)
            percentChange=round((valueChange/user_input)*100,2)
            tempData = {"now": now, "companyName": companyName, "user_input" : user_input,
                 "twoDaysData":twoDaysData['Close'][1],"valueChange":valueChange,"percentChange":percentChange, "error" :""}
            return render_template("index.html", **tempData)
             
        else:
            tempData = {"error":"You have entered wrong symbol"}
            return render_template("index.html", **tempData)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    # main()