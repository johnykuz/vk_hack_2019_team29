import React from 'react';
import PropTypes from 'prop-types';
import {Panel, Avatar, PanelHeader, List, Group, Div, Cell, platform, IOS} from '@vkontakte/vkui';
import './Profile.css'

const osname=platform();

const ProfileDefault = props => (
	<Panel id={props.id}>
		<PanelHeader>
            Профиль
		</PanelHeader>
		{
			<div className="profilePage">
				<div className="profileBackImage">
				<div className="userName">{props.fetchedUser.first_name+" "+props.fetchedUser.last_name}</div>
				<div className="cashbackText">
					Сумма кэшбэка 420 руб.
				</div>
				<div className="avatarContainer">
					<Avatar src={props.fetchedUser.photo_100} size={80}/>
				</div>
				</div>
				<div className="profileLoanRectangle" onClick={() => {window.location.href = "https://ib.psbank.ru/mp/credits/consumer-loan?formScroll=true&utm_source=newSitePSB"}}>
					<div className="profileLoanName">Взять рассрочку</div>
				</div>
				<div className="profileJoinRectangle" onClick={() => {window.location.href = "https://www.psbank.ru/Personal/Everyday/DebetCards"}}>
					<div className="profileJoinName">Cтать клиентом Промсвязьбанка</div>
				</div>
				<div className="profileAskRectangle" onClick={() => {window.location.href = "https://www.psbank.ru/Contact?from=ContactUs_Left"}}>
					<div className="profileAskName">Нажми, если есть вопросы</div>
				</div>
			</div>
		}
	</Panel>
)
ProfileDefault.propTypes = {
	id: PropTypes.string.isRequired,
    go: PropTypes.func.isRequired,
};

export default ProfileDefault;
