import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Home from './components/Home'; // Create Home component if not already done
import Recommendations from './components/Recommendations';
import FertilizerSuggestion from './components/FertilizerSuggestion'; // Create About component if not already done
import Sampling from './components/Sampling';

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/crop-recommendation" element={<Recommendations />} />
        <Route path="/fertilizer-recommendation" element={<FertilizerSuggestion />} />
        <Route path="/field-sampling" element={<Sampling />} />
      </Routes>
    </Router>
  );
};

export default App;
