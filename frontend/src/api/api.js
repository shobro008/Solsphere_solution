// src/api/api.js
import axios from 'axios';

const API_BASE = 'http://localhost:8000';  // your FastAPI backend URL

export const fetchMachines = () => axios.get(`${API_BASE}/machines`);

export const sendReport = (data) => axios.post(`${API_BASE}/report`, data);
