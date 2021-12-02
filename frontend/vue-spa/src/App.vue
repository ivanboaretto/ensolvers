<template>
  <div id='app' class='modal-vue'>
    <header>
      <h1>Tasks</h1>
    </header>
    <main>
      <div>
        <div v-for="todo in todo_list">
          <input v-on:click="updateCheckFor(todo)" type="checkbox" id="checkbox" v-bind:checked="todo.completed">
          <span>{{todo.description}}</span>
          <button v-on:click="openModalToUpdate(todo)">Update</button>
          <button v-on:click="deleteToDo(todo)">Delete</button>
        </div>

        <div class="overlay" v-if="show_modal" @click="show_modal = false"></div>
        <div class="modal" v-if="show_modal">
          <h3>Update ToDo</h3>
          <input v-model="update_description" placeholder="Input description" required/>
          <span>
            <button class="close" @click="show_modal = false">Close</button>
            <button class="close" @click="updateToDoWith()">Update</button>
          </span>
        </div>

        <input v-model="add_description" placeholder="Input description" required/>
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
      show_modal: false,
      endpoint: 'http://localhost:8000/todo_list',
      add_description: '',
      update_description: '',
      todo_to_update: null
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
      const postData = {description: this.add_description, completed: false};
      axios
        .post("http://localhost:8000/todo", postData)
        .then(this.getToDoList())
    },

    deleteToDo(todo){
      axios
        .delete("http://localhost:8000/todo/"+todo.id)
        .then(this.getToDoList())
    },

    openModalToUpdate(todo){
      this.todo_to_update = todo;
      this.show_modal = true;
    },

    updateToDoWith(){
      const putData = {description: this.update_description, completed: this.todo_to_update.completed}
      axios
        .put("http://localhost:8000/todo/"+this.todo_to_update.id,putData)
        .then(this.getToDoList())
      this.show_modal = false;
    },

    updateCheckFor(todo){
      const putData = {description: todo.description, completed: !todo.completed}
      axios
        .put("http://localhost:8000/todo/"+todo.id,putData)
        .then(this.getToDoList())
      this.show_modal = false;
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

/* Modal Style */
.modal-vue .overlay {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
}

.modal-vue .modal {
  position: relative;
  width: 300px;
  z-index: 9999;
  margin: 0 auto;
  padding: 20px 30px;
  background-color: whitesmoke;
}

.modal-vue .close{
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
