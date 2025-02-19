import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const login = (email, password) => axios.post(`${API_URL}/auth/login`, { email, password });
export const register = (data) => axios.post(`${API_URL}/auth/register`, data);
export const createContract = (data) => axios.post(`${API_URL}/contracts/create`, data);
export const checkCompliance = (data) => axios.post(`${API_URL}/compliance/check`, data);
export const filePatent = (data) => axios.post(`${API_URL}/ip-filing/file-patent`, data);
