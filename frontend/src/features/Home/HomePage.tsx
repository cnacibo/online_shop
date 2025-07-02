// src/pages/Orders/OrdersPage.tsx
import { useEffect, useState } from 'react';
import { MainLayout } from '../../components/Layout/MainLayout';
import shoppingImg from '../../assets/images/shopping.jpg';
import sadSeaGif from '../../assets/images/sad-sea.gif';
import plantPicture from '../../assets/images/plant.jpeg';
import shoppingBags from '../../assets/images/shopping2.jpg';
import './HomePage.css';

export const HomePage = () => {
  return (
      <MainLayout>
        <div className="home-content">
            <div className="home-container">
                <div className="home-text">
                    <h2>You can create an account and make orders that will be processed automatically</h2>
                </div>
                <div className="home-image">
                    <img src={shoppingImg} alt="Online shop" />
                </div>
            </div>
            <div className="button-grid">
                <div className="bags">
                    <img src={shoppingBags} alt="Online shop" />
                </div>
                <div className="buttons">
                    <button className="button-action"> Create account </button>
                    <button className="button-action"> Top up account </button>
                    <button className="button-action"> Check balance </button>
                    <button className="button-action"> Create order </button>
                    <button className="button-action"> View orders </button>
                    <button className="button-action"> Check status </button>
                </div>
            </div>

            <div className="plants">
                <img src={plantPicture} alt="Online shop" />
                <img src={plantPicture} alt="Online shop" />
                <img src={plantPicture} alt="Online shop" />
            </div>
            <div className="home-image">
                <img src={sadSeaGif} alt="Описание гифки"/>
            </div>
        </div>

      </MainLayout>
  );
};