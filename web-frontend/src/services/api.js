import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  auth: {
    username: "Sohomx",
    password: "Sohom@rpsb",
  },
});

// CSV upload
export const uploadCSV = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

// Fetch history
export const fetchHistory = () => {
  return API.get("history/");
};

