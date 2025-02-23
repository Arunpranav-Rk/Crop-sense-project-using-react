import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';


const Header = () => {
  return (
    <>
    <header className="header">
      <div className="logo">
        <img src="\logoimg.png" alt="Logo" className="logo-img" />
        Crop🌱 Sense 
      </div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/crop-recommendation">Crop Recommendation</Link></li>
          <li><Link to="/fertilizer-recommendation">Fertilizer Recommendation</Link></li>
          <li><Link to="/field-sampling">Field Sampling</Link></li>
        </ul>
      </nav>
    </header>
    </>
  );
};

export default Header;
