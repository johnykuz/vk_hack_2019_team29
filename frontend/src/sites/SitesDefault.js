import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, List, Group, Div, Cell, platform, IOS} from '@vkontakte/vkui';
import ProductScroller from './sub/ProductScroller'

const osname=platform();

const SitesDefault = props => (
	<Panel id={props.id}>
		<PanelHeader>
            Сайты
		</PanelHeader>
        <Group>
		<ProductScroller fetchProduct={(link) => {window.location.href = link}} endpoint="https://vkmarketplace.herokuapp.com/sites" hasMoreItemsTurnOff={true}/>
        </Group>
	</Panel>
)

SitesDefault.propTypes = {
	id: PropTypes.string.isRequired,
    go: PropTypes.func.isRequired,
};

export default SitesDefault;
