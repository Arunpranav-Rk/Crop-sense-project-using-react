import React, { useState } from 'react';
import './Recommendations.css';
import axios from 'axios';

const FertilizerSuggestion = () => {
  const [formData, setFormData] = useState({
    Nitrogen: '',
    Phosphorus: '',
    Potassium: '',
    Crop: ''
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const [showResult, setShowResult] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset error state

    try {
      const response = await axios.post('http://localhost:5000/predict_fertilizer', formData);
      setPrediction(response.data);
      setShowResult(true);
      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }
    }
    catch (error) {
      console.error('Error fetching fertilizer suggestions', error);
    }
  };


  return (
    <div className="recom-back">
      <div className="hero-recommendations">
        <h1>Fertilizer Suggestion</h1>
        {!showResult &&
          <>
            <p>Enter the following details to get a suggested fertilizer:</p>
            <div className="content-wrapper-recommendations">
              <div className="form-container-recommendations">
                <form onSubmit={handleSubmit}>
                  <label htmlFor="Nitrogen"><b>Nitrogen:</b></label>
                  <input
                    type="number"
                    step="0.01"
                    min="0"
                    max="1999"
                    id="Nitrogen"
                    name="Nitrogen"
                    value={formData.Nitrogen}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Phosphorus"><b>Phosphorus:</b></label>
                  <input
                    type="number"
                    step="0.01"
                    min="0"
                    max="1999"
                    id="Phosphorus"
                    name="Phosphorus"
                    value={formData.Phosphorus}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Potassium"><b>Potassium:</b></label>
                  <input
                    type="number"
                    step="0.01"
                    min="0"
                    max="1999"
                    id="Potassium"
                    name="Potassium"
                    value={formData.Potassium}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Crop"><b>Crop:</b></label>
                  <input
                    type="text"
                    id="Crop"
                    name="Crop"
                    value={formData.Crop}
                    onChange={handleChange}
                    required
                  /><br /><br />

                  <button type="submit">Get Suggested Fertilizer</button>
                </form>
              </div>
            </div>
          </>
        }
        {showResult && <>
          <div className="result-recommendations">
            <h2>Entered Data:</h2>
            <ul className="entered-data">
              {Object.entries(formData).map(([key, value]) => (
                <li key={key}>
                  <strong>{key}: </strong>{value}
                </li>
              ))}
            </ul>
            <div className="card-recommendations">
              <img src="fert/NPK.jpg" alt="Crop Image 1" />
              <div className="card-content-recommendations">
                <h2 className="card-title-recommendations">
                  {prediction.result || 'No Crop Suggested'}
                </h2>
                <p className="card-description-recommendations">
                  {prediction.description || 'No description available'}
                </p>
              </div>
            </div>
          </div>
        </>}
      </div>
    </div>
  );
};

export default FertilizerSuggestion;
