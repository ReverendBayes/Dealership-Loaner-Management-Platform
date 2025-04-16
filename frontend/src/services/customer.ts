// services/customer.ts
// Create and retrieve customer records from the backend

import axios from 'axios';

const API = '/api/customers';

export const createCustomer = async (payload: any) => {
  const res = await axios.post(`${API}/create`, payload);
  return res.data;
};

export const getCustomer = async (id: string) => {
  const res = await axios.get(`${API}/${id}`);
  return res.data;
};