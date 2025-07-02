import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:8000', // URL API Gateway
  headers: {
    'Content-Type': 'application/json',
  },
});