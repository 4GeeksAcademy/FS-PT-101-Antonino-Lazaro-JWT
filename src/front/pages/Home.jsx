import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { Register } from "../components/Register.jsx";

export const Home = () => {

	const { store, dispatch } = useGlobalReducer()

	return (
		<div className="text-center mt-5">
			<Register/>
		</div>
	);
}; 