# from cgi import test
# from distutils.log import debug
import pickle
import numpy
import pandas

# from flask import Flask,request
# from flask_restful import Resource,Api
# import pickle
# from flask_cors import CORS
import json


# app=Flask(__name__)

# CORS(app)
# api=Api(app)


def convert(str):
    try:
        new_str=str.replace("study interventions are ","")
        return new_str
    except:
        return str

def predict():
    # return 5
    
    solution=dict()
    # try:
    parsed=json.load(open('test.json'))
    # print(parsed)
    # print(parsed['patient1']['study'])
    # print(parsed.patient1['study'])
    # print(parsed.patient1['condition'])
    for i in range(1,2):
        patient=str("patient"+str(i))
        str1=parsed[patient]['study']
        str1=convert(str1)
        str2=parsed[patient]['condition']
        strin=convert(str1).lower()+str2.lower()
        # return str1
        study=str1
        similarity1=pickle.load(open('similarity11.pkl','rb'));
        df1=pickle.load(open('df11.pkl','rb'))
        # keys1=list()
        # keys1=df1.keys
        # print(keys1[0])
        # print(strin)

        try:
            study_index=df1[df1['keys']==strin].index[0]
            distance=similarity1[study_index]
                
            dis_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
            # except:
            #     print("some error")
            maxval=0
            for i in dis_list:
                if(df1.iloc[i[0]].qualification==1):
                    maxval=maxval+df1.iloc[i[0]].qualification
                else:
                    maxval-=1


            if maxval>0:
                # print("1")
                current_prediction=1
            else:
                # print("0")
                current_prediction=0
            
            solution[patient]=current_prediction
            # return current_prediction

        except:
            parsed=json.load(open('test.json'))
            # print(parsed.patient1['study'])
            # print(parsed.patient1['condition'])
            str2=""
            strin=convert(str1).lower()+" "+str2.lower()
            # return str1
            str1=parsed[patient]['study']
            str1=convert(str1)
            study=str1
            similarity=pickle.load(open('similarity.pkl','rb'));
            df=pickle.load(open('df.pkl','rb'))

            study_index=df[df['study']==study].index[0]
            distance=similarity[study_index]
                
            dis_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
            maxval=0
            for i in dis_list:
                if(df.iloc[i[0]].qualification==1):
                    maxval=maxval+df.iloc[i[0]].qualification
                else:
                    maxval-=1


            
            if maxval>0:
                # print("1")
                current_prediction=1
            else:
                # print("0")
                current_prediction=0
            
            # solution[patient]=current_prediction
            # return current_prediction
    # final_solution=solution.dump(solution)
    # with open('solution.json','w') as f:
    #     json.dump(solution,f)
    return current_prediction



if __name__=="__main__":
    k=predict()
    print(k)
    # return k
    # app.run(debug=True)