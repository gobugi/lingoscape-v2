import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import { authenticate } from "./store/session";
import Homepage from "./components/Homepage/Homepage";
import CreateDeck from "./components/CreateDeck/CreateDeck";
import AllDecks from "./components/AllDecks/AllDecks";
import Dashboard from "./components/Dashboard/Dashboard";
import SingleDeck from "./components/SingleDeck/SingleDeck";
import EditDeck from "./components/EditDeck/EditDeck";
import StudyDeck from "./components/StudyDeck/StudyDeck";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar loaded={loaded} />
      {loaded && (
        <Switch>
          <Route path="/" exact={true}>
            <Homepage />
          </Route>
          <ProtectedRoute path="/decks/new" exact={true}>
            <CreateDeck />
          </ProtectedRoute>
          <ProtectedRoute path="/decks/edit/:deckId" exact={true}>
            <EditDeck />
          </ProtectedRoute>
          <Route path="/decks/:deckId" exact={true}>
            <SingleDeck />
          </Route>
          <Route path="/decks/study/:deckId" exact={true}>
            <StudyDeck />
          </Route>
          <Route path="/decks" exact={true}>
            <AllDecks />
          </Route>
          <ProtectedRoute path="/dashboard" exact={true}>
            <Dashboard />
          </ProtectedRoute>
          <Route path="/login" exact={true}>
            <LoginForm />
          </Route>
          <Route path="/sign-up" exact={true}>
            <SignUpForm />
          </Route>
          <ProtectedRoute path="/users" exact={true}>
            <UsersList />
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true}>
            <User />
          </ProtectedRoute>
        </Switch>
      )}
    </BrowserRouter>
  );
}

export default App;
