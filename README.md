# fact-sheet-rag

## Introduction

This repository contains experiments defining and using the concept of a 'Fact Sheet'.

A Fact Sheet is a way to provide structured, personalised data as context to an LLM like ChatGPT or Llama.

## Usage

To generate a fact sheet, run

```sh
python convert-facts-to-json.py
```

The output will be called `facts.json`.

You can then paste this into your ChatGPT prompt, or use it with langchain in the example notebook, `lanchain-example.ipynb`.

## Adding new facts

To get started, you can add a text files stored in the `fact-sheets-txt` directory.

1. Name the file based on the type of facts (for example `house_work.txt`)

2. Add each fact on a new line. For example:
    ```
    I have to hoover the living room.

    The dishwasher needs emptying.
    ```

You can then run the commands as in the usage section above.
