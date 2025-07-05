//GET METHOD => HTTP
const express= require('express'); //importing the express package
const mongoose=require('mongoose');
const cors=require('cors');
const Todo=require('./MODEL/Todo');
const app=express();
app.use(express.json());
app.use(cors());
//mongodb://localhost:27017//TodoDB
mongoose.connect("mongodb://localhost:27017/TodoDB",{useNewUrlParser:true,useUnifiedTopology:true
    }).then(()=>{
        console.log("Connection established");
    }).catch(err=>{
        console.log("Error occured",err);
    });

app.get("/userlist",(req,res)=>{
    res.send("userlist method called...")
    
});


app.post("/dbaddtodo", async (req,res)=>{
    //const data = req.body;
    //res.send(data);
    //const newTask = new Todo({taskname:req.body.taskname});
    //newTask.save();
    //res.send(newTask);
    const newTask = new Todo({taskname:req.body.taskname});
    newTask.save();
    res.json(newTask);
});

app.get("/dbfetchtodo", async (req,res)=>{
    const tasks= await Todo.find();
    res.json(tasks);
});
app.put("/dbdatatodo",(req,res)=>{
    res.send("data method called...")
    
});
app.delete("/dbdeletetodo",(req,res)=>{
    res.send("delete method called...")
    
});
app.listen(5000,function(){
    console.log("port listening on 5000");
});

