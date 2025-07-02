import React from 'react';
import { OrdersPage } from '../features/Orders/OrdersPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HomePage } from '../features/Home/HomePage';
import {PaymentsPage} from "../features/Payments/PaymentsPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/orders" element={<OrdersPage />} />
        <Route path="/account" element={<PaymentsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
