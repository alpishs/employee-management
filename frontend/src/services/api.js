import axios from "axios";

const api = axios.create({
  baseURL: "https://employee-management-api.onrender.com",
});

export default api;