// services/agreement.ts
// Handles API calls for loaner agreement creation and retrieval

import axios from 'axios';

const API = '/api/agreements';

export const createAgreement = async (payload: any) => {
  const res = await axios.post(`${API}/create`, payload);
  return res.data;
};

export const getAgreement = async (id: string) => {
  const res = await axios.get(`${API}/${id}`);
  return res.data;
};

export const getAgreementsByCustomer = async (customerId: string) => {
  const res = await axios.get(`${API}/customer/${customerId}`);
  return res.data;
};