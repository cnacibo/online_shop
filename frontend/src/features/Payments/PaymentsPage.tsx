// src/pages/Orders/OrdersPage.tsx
import { useEffect, useState } from 'react';
import { MainLayout } from '../../components/Layout/MainLayout';
import {getPayments} from "../../shared/api/payments";

export const PaymentsPage = () => {

  return (
      <MainLayout>
        <div>
          <h2>My Account</h2>
        </div>
      </MainLayout>
  );
};