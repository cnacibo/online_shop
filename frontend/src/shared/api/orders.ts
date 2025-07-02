import { api } from './client';

export const getOrders = async (userId: string) => {
  const response = await api.get(`/orders?user_id=${userId}`);
  return response.data;
};

export const createOrder = async (data: { userId: string; items: string[] }) => {
  const response = await api.post('/orders', data);
  return response.data;
};