import React, { useState } from 'react';
import axios from 'axios';
import './Recommendations.css';

const Recommendations = () => {
  const [formData, setFormData] = useState({
    Nitrogen: '',
    Phosphorus: '',
    Potassium: '',
    SoilMoisture: '',
    Temperature: '',
    Humidity: '',
    Ph: '',
    Rainfall: ''
  });

  const [resultData, setResultData] = useState(null);
  const [showResult, setShowResult] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      setResultData(response.data);
      setShowResult(true);
    } catch (error) {
      console.error('Error fetching crop suggestions:', error);
    }
  };

  return (
    <div className="recom-back">
      <div className="hero-recommendations">
        <h1>Crop Suggestion</h1>
        {!showResult && (
          <>
            <p>Enter the following details to get a suggested crop:</p>
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

                  <label htmlFor="SoilMoisture"><b>Soil Moisture:</b></label>
                  <input
                    type="number"
                    step="1"
                    min="0"
                    max="1100"
                    id="SoilMoisture"
                    name="SoilMoisture"
                    value={formData.SoilMoisture}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Temperature"><b>Temperature Reading:</b></label>
                  <input
                    type="number"
                    step="0.1"
                    min="-20"
                    max="60"
                    id="Temperature"
                    name="Temperature"
                    value={formData.Temperature}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Humidity"><b>Humidity(%):</b></label>
                  <input
                    type="number"
                    step="1"
                    min="0"
                    max="100"
                    id="Humidity"
                    name="Humidity"
                    value={formData.Humidity}
                    onChange={handleChange}
                    required
                  /><br /><br />

                  <label htmlFor="Ph"><b>PH:</b></label>
                  <input
                    type="number"
                    step="0.01"
                    min="0"
                    max="14"
                    id="Ph"
                    name="Ph"
                    value={formData.Ph}
                    onChange={handleChange}
                  /><br /><br />

                  <label htmlFor="Rainfall"><b>Rainfall(mm):</b></label>
                  <input
                    type="number"
                    step="1"
                    min="0"
                    max="500"
                    id="Rainfall"
                    name="Rainfall"
                    value={formData.Rainfall}
                    onChange={handleChange}
                  /><br /><br />

                  <button type="submit">Get Suggested Crop</button>
                </form>
              </div>
            </div>
          </>
        )}
        {resultData && showResult && (
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
              <img src={resultData.resultImage1} alt="Crop Image 1" />
              <div className="card-content-recommendations">
                <h2 className="card-title-recommendations">
                  {resultData.result1 || 'No Crop Suggested'}
                </h2>
                <p className="card-description-recommendations">
                  {resultData.description1 || 'No description available'}
                </p>
              </div>
            </div>
            <div className="card-recommendations">
              <img src={resultData.resultImage2} alt="Crop Image 2" />
              <div className="card-content-recommendations">
                <h2 className="card-title-recommendations">
                  {resultData.result2 || 'No Crop Suggested'}
                </h2>
                <p className="card-description-recommendations">
                  {resultData.description2 || 'No description available'}
                </p>
              </div>
            </div>
            <div className="card-recommendations">
              <img src={resultData.resultImage3} alt="Crop Image 3" />
              <div className="card-content-recommendations">
                <h2 className="card-title-recommendations">
                  {resultData.result3 || 'No Crop Suggested'}
                </h2>
                <p className="card-description-recommendations">
                  {resultData.description3 || 'No description available'}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Recommendations;
