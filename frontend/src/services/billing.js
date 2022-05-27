import axios from 'axios';

class BillingDataService{

    getAllProducts(token){
        axios.defaults.headers.common["Authorization"] = "Token " + token;
        return axios.get("https://billing-system-simulator.herokuapp.com/api/product/");
    }

    deleteProduct(id, token){
        axios.defaults.headers.common["Authorization"] = "Token " + token;
        return axios.delete(`https://billing-system-simulator.herokuapp.com/api/product/${id}`);
    }
}

export default new BillingDataService();
