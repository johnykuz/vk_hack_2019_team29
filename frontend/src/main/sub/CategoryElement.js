import React from "react"

 const itemStyle = {
    flexShrink: 0,
    display: 'flex',
    flexDirection:'column',
    fontSize: 12,
    marginBottom: 10
 };

 const categoryImage = {
   width: 70,
   height: 92,
   left: 254,
   top: 120,
   marginLeft: 10,
   marginRight: 10,
   marginTop: 15,
   boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)"
  }
  

function CategoryElement(props){
	return (
   <div style={itemStyle}  onClick={() => {props.GetCategory(props.id)}}>
      <img style={categoryImage} src={props.cover}></img>
   </div>)
}

export default CategoryElement
