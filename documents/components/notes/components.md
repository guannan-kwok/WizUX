Figma Component Notes

What are Components
•	Components are ui elements reusable across design projects
o	Any time change main component: updates instances automatically to save time 
o	Faster workflow, more consistent design system, easier to collaborate with other designers 
•	The master component is created when you first turn a UI element into a component and defines the properties of the component.
•	The instance is a copy of the master component you can reuse across designs.
o	Instances are linked to master components. When you make changes to a master component it applies the changes to the instance.  An exception is instance overrides. 
o	In the layers panel you can identify which elements are master components and which are instances by the icon. Master components use a 4 diamond icon and instances use a single diamond icon.

Organizing and Structuring Components
 
•	1. Forward slash naming to create hierarchy
o	Example:
	Input/Field/Text — Active
	Input/Field/Text — Default
	Input/Field/Text — Disabled
	Input/Field/Text — Feedback
	Input/Field/Text — Filled
	Input/Field/Text — View Only
o	For access to a wider subcategory of “related components” in the instance menu you can combine the last two labels, ie. input type (text) and input status (default), by separating them with a dash instead of a slash. This is particularly useful for larger categories with many subcategories.
•	Group components in frames to better visualize (ex data table, date picker, dropdown as different frames)
 

•	2. Choose easy to understand method for structing component states and variations
o	Separate master components for each variation
	Fast to change state of instance, change multiple instances ast the same time, can save text overrides when updating state or variation, consistent 
	Downside: clutter
  

•	3. Use nested atomic components as global building blocks
o	The best approach for this is to create a set of reusable atomic components with the sole intention of nesting atomic instances inside other related components. 
	Take textfields as an example. We can turn a textfield’s shape into an atomic component and nest it’s instances inside every other textfield component we create. 
	This means all textfields use the exact same building block (i.e., the atomic instance) and if the shape of textfields were to change, all we’d need to do is update the atomic component and all other textfield components would update too.
	 Using an atomic approach allows you to seamlessly apply globalized changes to components which makes it much easier to maintain your system.




Working with Components
 
•	Set up constraints and layout grid to show responsive behavior of component as it is resized
•	Preserve text overrides on instance swaps 
o	To do this make sure the text layer within each component share the same name (e.g., “Button Text”). If you don’t do this your text overrides will not persist and you’ll need to manually update the text after you swap instances.
o	 
•	Use clip content to reduce repetitive instances
o	Toggle whether or not elements extend beyond the bounds of the component are cropped or hidden
o	 
•	Document components when hovering over it in the assets panel: provides context as to how it works and fits with the product 
•	Use instance overrides to adapt components
o	Override properties of instance without breaking link to master component
o	Can be used on text, color, effects (drop shadow, blur), advanced (size of component, swap nested instance, toggle on/off layers)
•	 
•	 
o	updates to master component do not revert overrides in first gif sequence above.
•	Reset overrirdes to go back to original properties
•	Swap components: 
o	Simply right click on the instance you want to switch and go to the Swap instance item. A submenu will appear with a list of related components.
•	Detach instance: want to make a new component, or unique element 


Figma Component Notes

What are Components
•	Components are ui elements reusable across design projects
o	Any time change main component: updates instances automatically to save time 
o	Faster workflow, more consistent design system, easier to collaborate with other designers 
•	The master component is created when you first turn a UI element into a component and defines the properties of the component.
•	The instance is a copy of the master component you can reuse across designs.
o	Instances are linked to master components. When you make changes to a master component it applies the changes to the instance.  An exception is instance overrides. 
o	In the layers panel you can identify which elements are master components and which are instances by the icon. Master components use a 4 diamond icon and instances use a single diamond icon.

Organizing and Structuring Components
 
•	1. Forward slash naming to create hierarchy
o	Example:
	Input/Field/Text — Active
	Input/Field/Text — Default
	Input/Field/Text — Disabled
	Input/Field/Text — Feedback
	Input/Field/Text — Filled
	Input/Field/Text — View Only
o	For access to a wider subcategory of “related components” in the instance menu you can combine the last two labels, ie. input type (text) and input status (default), by separating them with a dash instead of a slash. This is particularly useful for larger categories with many subcategories.
•	Group components in frames to better visualize (ex data table, date picker, dropdown as different frames)
 

•	2. Choose easy to understand method for structing component states and variations
o	Separate master components for each variation
	Fast to change state of instance, change multiple instances ast the same time, can save text overrides when updating state or variation, consistent 
	Downside: clutter
  

•	3. Use nested atomic components as global building blocks
o	The best approach for this is to create a set of reusable atomic components with the sole intention of nesting atomic instances inside other related components. 
	Take textfields as an example. We can turn a textfield’s shape into an atomic component and nest it’s instances inside every other textfield component we create. 
	This means all textfields use the exact same building block (i.e., the atomic instance) and if the shape of textfields were to change, all we’d need to do is update the atomic component and all other textfield components would update too.
	 Using an atomic approach allows you to seamlessly apply globalized changes to components which makes it much easier to maintain your system.




Working with Components
 
•	Set up constraints and layout grid to show responsive behavior of component as it is resized
•	Preserve text overrides on instance swaps 
o	To do this make sure the text layer within each component share the same name (e.g., “Button Text”). If you don’t do this your text overrides will not persist and you’ll need to manually update the text after you swap instances.
o	 
•	Use clip content to reduce repetitive instances
o	Toggle whether or not elements extend beyond the bounds of the component are cropped or hidden
o	 
•	Document components when hovering over it in the assets panel: provides context as to how it works and fits with the product 
•	Use instance overrides to adapt components
o	Override properties of instance without breaking link to master component
o	Can be used on text, color, effects (drop shadow, blur), advanced (size of component, swap nested instance, toggle on/off layers)
•	 
•	 
o	updates to master component do not revert overrides in first gif sequence above.
•	Reset overrirdes to go back to original properties
•	Swap components: 
o	Simply right click on the instance you want to switch and go to the Swap instance item. A submenu will appear with a list of related components.
•	Detach instance: want to make a new component, or unique element 


Accessibility (WCAG)
•	The Web Content Accessibility Guidelines (WCAG), developed by the World Wide Web Consortium, are technical standards that help make the digital world accessible to people with disabilities.
•	Principles (POUR)
o	Perceivable: Information must be perceivable to people using only one of their senses, so they understand all related content.
o	Operable: End users must be able to interact with all webpage elements. For instance, your website should be easily navigable with just a keyboard or voice controls for non-mouse users.
o	Understandable: The principle is just what it seems—end users must be able to understand web page content and functionality information.
o	Robust: Your website must effectively communicate information to all users, including users of assistive technologies, and remain compatible with evolving technologies and user needs.
The Three Levels of WCAG Conformance: A, AA, and AAA
There are three levels of conformance with WCAG guidelines:
•	A = the minimum level requirements any website should be able to meet.

Requirements include: 
o	Keyboard-only content access
o	Clearly labeled forms with instructions so users know what the forms require
o	Content compatibility with assistive technologies
o	Providing clear information or instructions in additional ways to using just shape, size, or color
•	AA = the mid-range conformance level that represents strong accessibility. It satisfies all Level A and Level AA criteria.

Requirements include: 
o	Text and background must have the proper color contrast (a minimum of 4.5 to 1)
o	Content organization must have a clear heading structure and follow a logical order (e.g., H1, H2, H3)
o	Navigation elements must be consistent throughout every webpage
•	AAA = the highest level of conformance, providing exceptional accessibility, but unachievable for certain content. It satisfies A, AA, and 28 additional criteria.

Requirements include:
o	A minimum of 7 to 1 contrast ratio for text and backgrounds
o	Sign language translation for pre-recorded video content
o	Expanded audio descriptions for pre-recorded video content
