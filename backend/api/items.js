import axios from 'axios';

const API_URL = 'http://192.168.x.x:8000/api/items/'; // ✅ replace with your LAN IP

export const getItems = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('API fetch error:', error);
    throw error;
  }
};
