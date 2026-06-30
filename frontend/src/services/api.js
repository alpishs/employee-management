import axios from "axios";

const api = axios.create({
  baseURL: "https://employee-management-api-8y57.onrender.com",
});

export default api;