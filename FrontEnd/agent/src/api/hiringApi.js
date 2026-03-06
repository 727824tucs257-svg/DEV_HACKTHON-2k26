import axios from "axios";

const response = await axios.post(
  "http://127.0.0.1:8000/run-hiring-agent",
  formData
);