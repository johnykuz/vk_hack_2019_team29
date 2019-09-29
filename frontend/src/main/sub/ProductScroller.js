import React from 'react'
import ProductCard from './ProductCard'
import InfiniteScroll from 'react-infinite-scroller';
import {Spinner} from '@vkontakte/vkui';
import Products from './Product.css'

class ProductScroller extends React.Component{
    
    constructor(props) {
        super(props);

        this.state = {
            products: [],
            hasMoreItems: true,
            hasMoreItemsTurnOff: this.props.hasMoreItemsTurnOff,
            count: 20,
            offset: 0,
            pageable: true, 
            endpoint: this.props.endpoint,
        };
        console.log("construct")
    }



    loadItems() {
        let url = this.props.endpoint//+"%5Boffset%5D="+this.state.offset; //ADD TERNARY



        console.log("Product "+this.state.endpoint)

        fetch(url)
        .then(response => response.json())
        .then(data => {
            // if(url!=this.state.endpoint){
            //     this.setState({
            //         products: [],
            //     })
            // }
            data.items.map((prod) => {
                this.state.products.push(prod);
            });
             //add offset if resource is pageable !!!!!!!!!!!!!!!!!!!!!!!!!!
            this.setState(prevState => {
                prevState.offset = prevState.offset + prevState.count
                return prevState;
            })
        })
        .catch((error) => {
            // Do something with the error object
          })

        if(this.state.hasMoreItemsTurnOff){
            this.setState({hasMoreItems : false})
        }
    }

    render() {
        const loader = <Spinner size="large" style={{paddingTop: 15,paddingBottom: 15}} />;
        
        var subjects = [];

        this.state.products.map(prod => {
            subjects.push(
                <ProductCard
			        id={prod.id}
    		        key={prod.id}
    		        name={prod.name}
                    cover={prod.photo_url}
                    price={prod.price}
                    fetchProduct={(id) => this.props.fetchProduct(id)}/>
            )
        })
        return (
            <InfiniteScroll
                pageStart={0}
                hasMore={this.state.hasMoreItems}
                loadMore={this.loadItems.bind(this)} //!!!!!!!!
                loader={loader}>

                <div className="products">
                    {subjects}
                </div>
            </InfiniteScroll>
        );
    }
}

export default ProductScroller