# Parameters
INJECT_LANGUAGE = "Typescript (TSX)"
INJECT_FRAMEWORK_FROM = "Vue 2.0"
INJECT_FRAMEWORK_TO = "React"
INJECT_LANGUAGE_STORY = "Typescript"

# Templates
TEMPLATE_V1 = """You are a web developer experienced in {language}, {framework_from} and {framework_to}.

Here is the following UI component in {framework_from}:
```
{code_from}
```

You need to convert it into a UI component in {framework_to}:

1. Also preserve variable names where possible.
2. Utilize the following UI libraries for the conversion, especially when it comes to replacing components from 'vuetify' in {framework_from}:
- @mui/material 
- @emotion/react 
- @emotion/styled
3. Insert comments where necessary.
4. Ensure that the output is in {language}.

3. Here's a template as to how you should structure your code:
```
{output_structure_template}
```

"""


TEMPLATE_STORY_V1 = """You are a web developer experienced in {language} and Storybook for {framework_to}.
You are tasked with creating a storybook story for the component below:
```
{code_new}
```
Here's a template as to how you should structure your code:
```
{output_structure_template_story}
```

Ensure that the output in in {language}.
"""


# Structure Templates

INJECT_OUTPUT_STRUCTURE_TEMPLATE = r"""iimport React from 'react';

interface <ComponentName>Props {
    ...
}

function <ComponentName>({  ...props }: <ComponentName>Props) {

    ...

    return (
       ...
    );
}

export default <ComponentName>;
"""


INJECT_OUTPUT_STRUCTURE_TEMPLATE_STORY = r"""
import <ComponentName> from './<ComponentName>';

// More on how to set up stories at: https://storybook.js.org/docs/react/writing-stories/introduction
const meta: Meta<typeof ActionButton> = {
  title: 'Components/<ComponentName>',
  component: <ComponentName>,
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof <ComponentName>>;

// More on writing stories with args: https://storybook.js.org/docs/react/writing-stories/args
export const Primary: Story = {
  args: {
    ...
  },
};

"""
