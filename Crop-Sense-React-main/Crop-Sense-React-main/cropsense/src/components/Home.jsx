import React from 'react';
import './Home.css';

const Home = () => {
    return (
        <div className="home-content">
            <div className="hero">
                <div className="hero-content">
                    <h1>Welcome to Crop Sense</h1>
                    <div className="header-info">
                        <p>Explore modern agriculture techniques! Crop Sense helps you optimize crop yield and resource usage with real-time recommendations and innovative technology.</p>
                    </div>
                </div>
            </div>
            <section className="features">
                <h2>Our Features</h2>
                <div className="feature-item">
                    <img src="/crop1.png" alt="Smart Crop Recommendations" />
                    <p>Using advanced machine learning algorithms, Crop Sense analyzes soil, weather, and crop data to provide you with the best crop choices for your specific conditions.</p>
                </div>
                <div className="feature-item">
                    <img src="/crop2.png" alt="Fertilizer Suggestions" />
                    <p>Crop Sense offers detailed fertilizer suggestions tailored to your soil's nutrient needs, ensuring your crops get the right nutrients at the right time.</p>
                </div>
                <div className="feature-item">
                    <img src="/crop3.png" alt="Field Sampling" />
                    <p>Accurate field sampling is crucial for understanding your soil's health. Crop Sense provides step-by-step guides and tools to help you collect and analyze soil samples.</p>
                </div>
            </section>
            <div className="content-down">
                <div className="foot-content">
                    <div className="about-mission">
                        <section className="about">
                            <h2>About Us</h2>
                            <p>Crop Sense provides farmers with modern solutions for optimizing crop yield and resource usage. Our innovative technology offers real-time recommendations and insights to help you achieve the best results.</p>
                        </section>
                        <section className="mission">
                            <h2>Our Mission</h2>
                            <p>At Crop Sense, our mission is to revolutionize agriculture by providing farmers with the tools and knowledge they need to thrive. We harness the power of technology to offer personalized crop recommendations, ensuring sustainable and efficient farming practices.</p>
                        </section>
                    </div>
                </div>
                <section className="how-it-works">
                    <h2>How It Works</h2>
                    <div className="step">
                        <h3>Step 1: Input Your Data</h3>
                        <p>Start by entering key data about your farm, including soil composition, weather conditions, and current crops. Our easy-to-use interface makes data entry quick and hassle-free.</p>
                    </div>
                    <div className="step">
                        <h3>Step 2: Receive Recommendations</h3>
                        <p>Based on the data you provide, Crop Sense generates personalized crop and fertilizer recommendations. Our algorithms consider various factors to ensure the best possible advice for your specific situation.</p>
                    </div>
                    <div className="step">
                        <h3>Step 3: Implement and Monitor</h3>
                        <p>Follow our recommendations to plant and care for your crops. Crop Sense offers ongoing support and monitoring tools to help you track progress and make adjustments as needed.</p>
                    </div>
                </section>
                <section className="contact">
                    <h2>Contact Us</h2>
                    <p>Have any questions? Feel free to reach out to us.</p>
                    <form>
                        <input type="text" placeholder="Your Name" required />
                        <input type="email" placeholder="Your Email" required />
                        <textarea placeholder="Your Message" required></textarea>
                        <button type="submit">Send Message</button>
                    </form>
                </section>
            </div>
            <footer>
                &copy; {new Date().getFullYear()} Crop Sense. All rights reserved.
            </footer>
        </div>
    );
};

export default Home;
