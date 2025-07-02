import { api } from './client';

export const getPayments = async (userId: string) => {
  const response = await api.get(`/payments?user_id=${userId}`);
  return response.data;
};

export {};