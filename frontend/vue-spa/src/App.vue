<template>
  <div id='app'>
    <header>
      <h1>Tasks</h1>
    </header>
    <main>
      <div>
        <div v-for="todo in todo_list">
          <input type="checkbox" id="checkbox">
          <span>{{todo.description}}</span>
          <button v-on:click="updateToDoWith(todo)">Update</button>
          <button v-on:click="deleteToDo(todo)">Delete</button>
        </div>
        <input v-model="description" placeholder="Input TODO" required/>
        <button v-on:click="addToDo()">Add</button>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todo_list: null,
      endpoint: 'http://localhost:8000/todo_list',
      description: ''
    }
  },

  created() {
    this.getToDoList();
  },

  methods: {
    getToDoList(){
      axios.get(this.endpoint)
        .then(response => {
          this.todo_list = response.data;
        })
        .catch(error => {
          console.log('Error fetching the To Do List');
          console.log(error);
        })
    },

    addToDo(){
      const postData = {description: this.description, completed: false};
      axios
        .post("http://localhost:8000/todo", postData)
        .then(this.getToDoList())
    },

    deleteToDo(todo){
      axios
        .delete("http://localhost:8000/todo/"+todo.id)
        .then(this.getToDoList())
    },

    updateToDoWith(todo){
      
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
