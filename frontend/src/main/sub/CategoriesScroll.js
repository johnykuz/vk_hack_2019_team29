import React from "react"
import CategoryElement from "./CategoryElement"
import {HorizontalScroll, Group, Div, Cell} from '@vkontakte/vkui';
import categoriesData from './categoriesData'

class CategoriesScroll extends React.Component{
	render(){
		let subjects = categoriesData.map(prod => <CategoryElement 
			id={prod.id}
    		key={prod.id}
    		name={prod.name}
			cover={prod.cover}
			GetCategory={(id) => this.props.GetCategory(id)}/>)
			
		const horizontalScrollBack = {
			display: 'flex',
			backgroundImage: "url(https://i.ibb.co/Ld04557/bg-cat-2.png)",
			// left: 0%;
			// right: 0%;
			// top: 0%;
			// bottom: 0%;
			height: '8em',
			backgroundSize: 'contain',
			backgroundRepeat: 'no-repeat',
			backgroundPosition: 'right',
		
		};
			

      return (
		<div style = {horizontalScrollBack}>
          <HorizontalScroll>
            <div style={{display:"flex"}}>
					{subjects}
            </div>
          </HorizontalScroll>
		</div>
   	 	)
      }
	
}

export default CategoriesScroll