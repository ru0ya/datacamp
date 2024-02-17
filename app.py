from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)

@app.route('/house_prediction', methods=['POST', 'GET'])
def house_prediction():
       if request.method == 'POST':
            #  selling_price = request.form['selling_price']  
            try:
                  bedrooms = request.form['no_bedrooms']
                  location = request.form['location']
                  house_type = request.form['house_type']
                  generator = request.form['back_up_generator'] 
                  en_suite = request.form['en_suite']
                  garden = request.form['garden']
                  gym = request.form['gym']
                  dsq = request.form['Dsq']
                  pool = request.form['pool']
                  if en_suite == 'Yes':
                        en_suite = 1
                  else: 
                        en_suite = 0
                  if garden == 'Yes':
                        garden = 1
                  else: 
                        garden = 0
                  if gym == 'Yes':
                        gym = 1
                  else: 
                        gym = 0
                  if pool == 'Yes':
                        pool = 1
                  else:
                        pool = 0
                  if generator == 'Yes':
                        generator = 1
                  else:
                        generator = 0
                  if dsq == 'Yes':
                        dsq = 1
                  else:
                        dsq = 0
                        
                  
            
                  # Load the model
                  model,  preprocessor= pickle.load(open('preprocessor.pkl', 'rb'))
                  # Make prediction
                  data = preprocessor.transform([[bedrooms, location, house_type, generator, en_suite, garden, gym, pool, dsq]])
                  prediction = model.predict(data)
                  return render_template('index.html', prediction_text='The price of the house is Kshs. {}'.format(prediction))
            except Exception as e:
                  print(str(e))
                  return render_template('index.html', prediction_text=f'Please fill in all the fields {str(e)}')
       else:
             return render_template('index.html')
       
if __name__ == '__main__':
      app.run(debug=True)
       
