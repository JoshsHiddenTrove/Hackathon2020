import smartmonkey

from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
#num monkeys = args[0]
#mutation = args[1]
#interval = args[2]
# Newpop(
#     NewGoal
#     NewNgram
def show_front():
    if(request.method == "GET"):
        if(len(request.args.to_dict()) > 0):
            print(request.args)
            smartmonkey.Newpop(request.args.get('num_monkeys'))
            smartmonkey.NewGoal(request.args.get('mutation'))
            smartmonkey.NewNgram(request.args.get('interval'))
            work = smartmonkey.NewGoal(request.args.get('text'))

            print(work)

            result = smartmonkey.retres()
            print(result)
            print(result)
            
            
            return render_template('front.html', d = result)
    
    return render_template('front.html')


if __name__ == '__main__':
    t = smartmonkey.Individual("helloWord")
    smartmonkey.main()
    app.run()