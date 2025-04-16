// services/insurance.ts
// Uploads insurance screenshot and returns parsed validation

import axios from 'axios';

const API = '/api/insurance';

export const verifyInsurance = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);

  const res = await axios.post(`${API}/verify`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });

  return res.data;
};