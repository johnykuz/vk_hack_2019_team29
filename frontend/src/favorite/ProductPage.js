import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, Link, PanelHeaderContent, List, Cell, HorizontalScroll , HeaderButton, Group, Div, platform, IOS} from '@vkontakte/vkui';
import Icon28ChevronBack from '@vkontakte/icons/dist/28/chevron_back';
import Icon24Back from '@vkontakte/icons/dist/24/back';



const osname=platform();

const ProductPage = props => (
	<Panel id={props.id}>
		<PanelHeader
			left={
				<HeaderButton onClick={props.go} data-to={props.wasActivePanel}>
					{osname === IOS ? <Icon28ChevronBack/> : <Icon24Back/>}
				</HeaderButton>
			}>
			<PanelHeaderContent>
                {props.product.name.substring(0, 15)}
			</PanelHeaderContent>
		</PanelHeader>
        <div className="p">
        <img className="p" src={props.product.cover} alt="{props.name} image"/>
        <div className="p">{props.product.description}</div>
        <div className="p">{props.product.price}</div>
        </div>)
	</Panel>
)

ProductPage.propTypes = {
	id: PropTypes.string.isRequired,
    go: PropTypes.func.isRequired,
    product: PropTypes.object.isRequired,
};

export default ProductPage