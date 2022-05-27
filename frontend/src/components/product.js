import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import ListGroup from 'react-bootstrap/ListGroup';
import ListGroupItem from 'react-bootstrap/ListGroupItem';
import Stack from 'react-bootstrap/Stack';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';


import BillingDataService from '../services/billing';

const ProductList = props => {

    
    const [products, setProducts] = useState([]);

    //console.log(props);

    useEffect(() =>{
        retrieveProducts();
    }, [props.token]);
    
    const retrieveProducts = () => {
        if(props.token){
            BillingDataService.getAllProducts(props.token)
            .then(response => {
                setProducts(response.data);
            })
            .catch( e => {
                console.log(e);
            });
        }
    }

    const deleteProduct = (productId) =>{
        BillingDataService.deleteProduct(productId, props.token)
            .then(response => {
            retrieveProducts();
            })
            .catch(e =>{
            console.log(e);
            });
    }

    return (
        <Container>
            {props.token == null || props.token === "" ? (
                <Alert variant='warning'>
                You are not logged in. Please <Link to={"/login"}>login</Link> to see your todos.
                </Alert>
                ) : (   
                    <Row xs={1} md={5} className="g-4">
                        {products.map((product) => (
                            <Col>
                                <Card>
                                    <Card.Img variant="top" src={product.imageurl} height="180px" />
                                    <Card.Body>
                                        <Card.Title>{product.name}</Card.Title>
                                        <Card.Text>
                                            {product.description.substring(0, 50)}
                                        </Card.Text>
                                    </Card.Body>
                                    <ListGroup className="list-group-flush">
                                        <ListGroupItem>codigo: {product.code}</ListGroupItem>
                                        <ListGroupItem>Precio sugerido: L.{product.suggested_public_price}</ListGroupItem>
                                    </ListGroup>
                                    <Card.Body>
                                        <Card.Link href="#">agregar</Card.Link>
                                        <Card.Link href="#">opciones</Card.Link>
                                    </Card.Body>
                                </Card>
                            </Col>
                        ))}
                    </Row>
            )}
        </Container>
    );
}

export default ProductList;