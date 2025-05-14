from flask import Flask,render_template,request,session
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
app=Flask(__name__)
app.secret_key='sunil18'
llm=ChatMistralAI(model="mistral-tiny",temperature=1.0)
@app.route('/',methods=['GET','POST'])
def index():
    if 'history' not in session:
        session['history']=[]
    result=""
    if request.method=='POST':
        query=request.form['query']
        memory=ConversationBufferMemory()
        for q,a in session['history']:
            memory.chat_memory.add_user_message(q)
            memory.chat_memory.add_ai_message(a)
        conversation=ConversationChain(llm=llm,memory=memory)
        result=conversation.run(query)
        session['history'].append((query,result))
        session.modified=True
    return render_template('index.html',result=result,history=session.get('history',[]))
if __name__ == '__main__':
    app.run(debug=True)