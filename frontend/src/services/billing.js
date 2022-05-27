import axios from 'axios';

class BillingDataService{

    getAllProducts(token){
        axios.defaults.headers.common["Authorization"] = "Token " + token;
        return axios.get("http://localhost:8000/api/product/");
    }

    deleteProduct(id, token){
        axios.defaults.headers.common["Authorization"] = "Token " + token;
        return axios.delete(`http://localhost:8000/api/product/${id}`);
    }
}

export default new BillingDataService();
