import { useState } from "react";
import linge from '../Assets/linge.png'
import Navbar from "../utils/navBarre";

const Panier = () => {

    const prix = 50000

    const [nbre, setNbre] = useState(1)      
    const add = () => {
        setNbre(nbre + 1)
    }
    const remove = () => {
        if (nbre > 1) {
            setNbre(nbre - 1)
        }else{
            setNbre(1)
        }
    }

    return (

        <>

            <Navbar />
            <div className="panier-container">
                <h1>Votre Panier</h1>
                <div className="panier-items">
                    <div className="panier-item">
                        <img src={linge} alt="Nom du produit" />
                        <div className="item-details">
                            <h2>Nom du Produit</h2>
                            <p>Prix: {prix} FCFA</p>
                            <div className="quantity-controls">
                                <button onClick={remove}>-</button>
                                <span>{nbre}</span>
                                <button onClick={add}>+</button>
                            </div>
                        </div>
                        <button className="remove-item">Supprimer</button>
                    </div>
                </div>
                <div className="panier-summary">
                    <h2>Résumé de la commande</h2>
                    <p>Total: {prix * nbre} FCFA</p>
                    <button className="checkout-button">Passer la commande</button>
                </div>
            </div>
        </>
        
    );


}

export default Panier