from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

# Importing model
model = pickle.load(open(r'D:\Crop Sense React\random_forest_model.pkl', 'rb'))
sc = pickle.load(open(r'D:\Crop Sense React\standscaler.pkl', 'rb'))
ms = pickle.load(open(r'D:\Crop Sense React\minmaxscaler.pkl', 'rb'))
model2 = pickle.load(open(r"D:\Crop Sense React\recommendation_model.pkl", "rb"))
lbl_enc = pickle.load(open(r"D:\Crop Sense React\crop_label_encoder.pkl", "rb"))
fert_lbl_enc = pickle.load(open(r"D:\Crop Sense React\fertilizer_label_encoder.pkl", "rb"))

# Creating Flask app
app = Flask(__name__, static_folder="static")
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    N = float(data['Nitrogen'])
    P = float(data['Phosphorus'])
    K = float(data['Potassium'])
    temp = float(data['Temperature'])
    humidity = float(data['Humidity'])
    ph = float(data['Ph'])
    rainfall = float(data['Rainfall'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    # Scaling the input features
    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)

    # Predicting probabilities
    probabilities = model.predict_proba(final_features)[0]

    # Sorting and selecting top 3 indices
    top_3_indices = np.argsort(probabilities)[-3:][::-1]

    # Mapping indices to crop names
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    result_image = {1: "crops/Rice.jpeg",
                    2: "crops/Maize.jpeg",
                    3: "crops/Jute.jpeg",
                    4: "crops/Cotton.jpeg",
                    5: "crops/Coconut.jpeg",
                    6: "crops/Papaya.jpeg",
                    7: "crops/Orange.jpeg",
                    8: "crops/Apple.jpeg",
                    9: "crops/Muskmelon.jpeg",
                    10: "crops/Watermelon.jpeg",
                    11: "crops/Grapes.jpeg",
                    12: "crops/Mango.jpeg",
                    13: "crops/Banana.jpeg",
                    14: "crops/Pomegranate.jpeg",
                    15: "crops/Lentil.jpeg",
                    16: "crops/Blackgram.jpeg",
                    17: "crops/Mungbean.jpeg",
                    18: "crops/Mothbeans.jpeg",
                    19: "crops/Pigeonpeas.jpeg",
                    20: "crops/Kidneybeans.jpeg",
                    21: "crops/Chickpea.jpeg",
                    22: "crops/Coffee.jpeg"
                }

    crop_description = {"Rice" : "Rice is predominantly cultivated in Asia, especially in regions like China, India, and Southeast Asia. It thrives in clayey, loamy soils that retain water well." ,
                        "Maize" : "Maize, or corn, is widely grown in the United States, Brazil, and China. It prefers well-drained, fertile loamy soils rich in organic matter." , 
                        "Jute" : "Jute is mainly cultivated in Bangladesh and India, particularly in the Ganges Delta. It grows best in alluvial soil with a high clay content." , 
                        "Cotton" : "Cotton is densely grown in India, the United States, and China. It favors deep, well-drained sandy loam soils with a slightly acidic to neutral pH." , 
                        "Coconut" : "Coconut palms are most commonly found in tropical coastal regions like Indonesia, the Philippines, and India. They grow well in sandy, loamy, or alluvial soils that are well-drained." , 
                        "Papaya" : "Papaya is extensively grown in India, Brazil, and Mexico. It thrives in well-drained sandy loam or alluvial soils rich in organic matter." , 
                        "Orange" : "Oranges are primarily cultivated in Brazil, the United States (especially Florida), and China. They prefer well-drained sandy loam soils rich in organic content." ,
                        "Apple" : " Apples are widely grown in temperate regions like the United States, China, and Europe. They thrive in well-drained loamy soils with a slightly acidic pH." , 
                        "Muskmelon" : "Muskmelon is grown in warmer climates such as in India and the United States. It prefers sandy loam soils that are well-drained and rich in organic matter." , 
                        "Watermelon" : "Watermelon is cultivated in warm regions like China, Turkey, and the United States. It grows best in sandy loam soils with good drainage and moderate organic content." , 
                        "Grapes" : "Grapes are primarily cultivated in Mediterranean climates like those found in Italy, Spain, and France. They thrive in well-drained loamy or sandy loam soils with good fertility." , 
                        "Mango" : "Mangoes are extensively grown in India, Thailand, and Mexico. They favor well-drained alluvial or loamy soils rich in organic matter." , 
                        "Banana" : "Bananas are widely cultivated in tropical regions such as India, Brazil, and Ecuador. They thrive in well-drained loamy soils with high organic content." ,
                        "Pomegranate" : "Pomegranates are primarily grown in India, Iran, and the Mediterranean. They prefer well-drained sandy or loamy soils with a neutral to slightly alkaline pH." , 
                        "Lentil" : "Lentils are commonly grown in Canada, India, and Turkey. They thrive in well-drained loamy or sandy loam soils with moderate fertility." , 
                        "Blackgram" : "Blackgram is densely cultivated in India and Myanmar. It grows well in loamy soils that are well-drained and rich in organic matter." , 
                        "Mungbean" : "Mungbeans are widely grown in India, China, and Southeast Asia. They prefer well-drained sandy loam or loamy soils with good fertility." , 
                        "Mothbeans" : "Mothbeans are commonly grown in arid regions like Rajasthan, India. They thrive in sandy loam soils that are well-drained and drought-resistant." ,
                        "Pigeonpeas" : "Pigeonpeas are extensively grown in India, Eastern Africa, and the Caribbean. They grow best in well-drained loamy soils with moderate fertility." , 
                        "Kidneybeans" : "Kidneybeans are cultivated in the United States, Brazil, and India. They thrive in well-drained loamy soils rich in organic matter." , 
                        "Chickpea" : "Chickpeas are primarily grown in India, Australia, and Turkey. They prefer well-drained loamy or sandy loam soils with moderate fertility." , 
                        "Coffee" : "Coffee is grown in tropical regions like Brazil, Vietnam, and Colombia. It thrives in well-drained loamy soils rich in organic content and slightly acidic pH."}

    top_3_crops = [list(crop_dict.values())[list(crop_dict.keys()).index(i + 1)] for i in top_3_indices]

    # Temp variables for crops
    crop1 = top_3_crops[0]
    crop2 = top_3_crops[1]
    crop3 = top_3_crops[2]
    # Formatting the result
    result1 = "{}".format(crop1)
    result2 = "{}".format(crop2)
    result3 = "{}".format(crop3)

    description1 = "{}".format(crop_description[crop1])
    description2 = "{}".format(crop_description[crop2])
    description3 = "{}".format(crop_description[crop3])

    def get_key_by_value(dictionary, value):
        result = {k: v for k, v in dictionary.items() if v == value}
        if result:
            return next(iter(result))
        return None
    key1 = get_key_by_value(crop_dict, crop1)
    key2 = get_key_by_value(crop_dict, crop2)
    key3 = get_key_by_value(crop_dict, crop3)

    response = {
        'result1': result1,
        'result2': result2,
        'result3': result3,
        'description1': description1,
        'description2': description2,
        'description3': description3,
        'resultImage1': result_image[key1],
        'resultImage2': result_image[key2],
        'resultImage3': result_image[key3]
    }

    return jsonify(response)

@app.route('/predict_fertilizer', methods=['POST'])
def predict_fertilizer():
    data = request.get_json()
    nitrogen = float(data['Nitrogen'])
    phosphorus = float(data['Phosphorus'])
    potassium = float(data['Potassium'])
    crop = data['Crop'].strip()

    # Encode the crop
    crop_encoded = lbl_enc.transform([crop])[0]

    # Prepare input for the model
    input_features = np.array([[nitrogen, phosphorus, potassium, crop_encoded]])

    # Predict fertilizer
    fertilizer_index = model2.predict(input_features)[0]
    fertilizer_name = fert_lbl_enc.inverse_transform([fertilizer_index])[0]

    result = {
        1: "Urea",
        2: "DAP",
        3: "MOP",
        4: "10:26:26 NPK",
        5: "SSP",
        6: "Magnesium Sulphate",
        7: "13:32:26 NPK",
        8: "12:32:16 NPK",
        9: "50:26:26 NPK",
        10: "19:19:19 NPK",
        11: "Chelated Micronutrient",
        12: "18:46:00 NPK",
        13: "Sulphur",
        14: "20:20:20 NPK",
        15: "Ammonium Sulphate",
        16: "Ferrous Sulphate",
        17: "White Potash",
        18: "10:10:10 NPK",
        19: "Hydrated Lime"
    }

    description = {
        "Urea": "Urea is a highly concentrated nitrogen fertilizer, widely used for promoting rapid vegetative growth in plants. It is cost-effective and works well in a variety of soils.",
        "DAP": "Diammonium Phosphate (DAP) is a popular phosphorus fertilizer that also supplies nitrogen, essential for early plant growth and root development.",
        "MOP": "Muriate of Potash (MOP) is a potassium-rich fertilizer, improving overall plant health, drought resistance, and crop quality.",
        "10:26:26 NPK": "This NPK blend provides a balanced supply of nitrogen, phosphorus, and potassium, ideal for boosting root and flower development.",
        "SSP": "Single Super Phosphate (SSP) is a phosphorus fertilizer that also contains sulfur, improving root strength and overall growth.",
        "Magnesium Sulphate": "Magnesium Sulphate supplies magnesium and sulfur, enhancing chlorophyll production and overall plant vigor.",
        "13:32:26 NPK": "This NPK ratio offers high phosphorus content, suitable for flowering and fruiting stages of crop development.",
        "12:32:16 NPK": "An NPK fertilizer with a focus on phosphorus for root development and nitrogen for early plant growth.",
        "50:26:26 NPK": "This fertilizer provides a high nitrogen ratio, supporting leafy growth while maintaining balanced phosphorus and potassium levels.",
        "19:19:19 NPK": "A balanced NPK fertilizer, ideal for all stages of plant growth, providing equal nitrogen, phosphorus, and potassium.",
        "Chelated Micronutrient": "Chelated micronutrients ensure optimal absorption of essential trace elements like iron, zinc, and manganese for plant health.",
        "18:46:00 NPK": "This fertilizer is rich in phosphorus and nitrogen, supporting early-stage crop growth and root development.",
        "Sulphur": "Sulphur improves protein synthesis and nutrient uptake in plants, crucial for oilseed crops and legumes.",
        "20:20:20 NPK": "A perfectly balanced NPK fertilizer for general-purpose use, supporting plant growth, flowering, and fruiting.",
        "Ammonium Sulphate": "Ammonium Sulphate is a nitrogen fertilizer with sulfur, suitable for acid-loving crops and improving soil pH.",
        "Ferrous Sulphate": "Ferrous Sulphate supplies iron and sulfur, preventing iron chlorosis and promoting healthy green foliage.",
        "White Potash": "White Potash is a potassium-rich fertilizer that improves stress tolerance and enhances fruit quality.",
        "10:10:10 NPK": "A balanced fertilizer providing equal parts nitrogen, phosphorus, and potassium, suitable for general-purpose gardening.",
        "Hydrated Lime": "Hydrated Lime is used to adjust soil pH, reduce acidity, and enhance calcium availability for plants."
    }

    result_fertilizer = {
        1: "fert/Urea.jpg",
        2: "fert/DAP.jpg",
        3: "fert/MOP.jpg",
        4: "fert/NPK.jpg",
        5: "fert/SSP.jpg",
        6: "fert/Magnesium-Sulphate.jpg",
        7: "fert/NPK.jpg",
        8: "fert/NPK.jpg",
        9: "fert/NPK.jpg",
        10: "fert/NPK.jpg",
        11: "fert/Chelated-Micronutrient.jpeg",
        12: "fert/NPK.jpg",
        13: "fert/Sulphur.jpg",
        14: "fert/NPK.jpg",
        15: "fert/Ammonium-Sulphate.jpg",
        16: "fert/Ferrous-Sulphate.jpg",
        17: "fert/White-Potash.jpg",
        18: "fert/NPK.jpg",
        19: "fert/Hydrated-lime.jpg"
    }

    #key = {k for k, v in result.items() if v == fertilizer_name}

    fert_response = {
        'result': fertilizer_name,
        'description': description[fertilizer_name]
        #'imagef': result_fertilizer[key]
    }

    return jsonify(fert_response)

if __name__ == "__main__":
    app.run(debug=True)