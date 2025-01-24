import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/api', // Flask
    // baseURL: 'http://127.0.0.1:8000/api', // Django
});

export default api;
