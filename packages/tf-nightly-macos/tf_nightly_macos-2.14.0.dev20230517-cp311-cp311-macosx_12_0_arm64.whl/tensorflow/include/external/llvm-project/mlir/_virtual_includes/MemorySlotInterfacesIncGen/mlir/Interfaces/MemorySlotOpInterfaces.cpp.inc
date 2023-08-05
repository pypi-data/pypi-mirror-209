/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Definitions                                                      *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

/// Returns a list of memory slots for which promotion should be attempted.
/// This only considers the local semantics of the allocator, ignoring
/// whether the slot pointer is properly used or not. This allocator is the
/// "owner" of the returned slots, meaning no two allocators should return
/// the same slot. The content of the memory slot must only be reachable
/// using loads and stores to the provided slot pointer, no aliasing is
/// allowed.
/// 
/// Promotion of the slot will lead to the slot pointer no longer being
/// used, leaving the content of the memory slot unreachable.
/// 
/// No IR mutation is allowed in this method.
::llvm::SmallVector<::mlir::MemorySlot> mlir::PromotableAllocationOpInterface::getPromotableSlots() {
      return getImpl()->getPromotableSlots(getImpl(), getOperation());
  }
/// Provides the default Value of this memory slot. The provided Value
/// will be used as the reaching definition of loads done before any store.
/// This Value must outlive the promotion and dominate all the uses of this
/// slot's pointer. The provided rewriter can be used to create the default
/// value on the fly.
/// 
/// The rewriter is located at the beginning of the block where the slot
/// pointer is defined. All IR mutations must happen through the rewriter.
::mlir::Value mlir::PromotableAllocationOpInterface::getDefaultValue(const ::mlir::MemorySlot & slot, ::mlir::RewriterBase & rewriter) {
      return getImpl()->getDefaultValue(getImpl(), getOperation(), slot, rewriter);
  }
/// Hook triggered for every new block argument added to a block.
/// This will only be called for slots declared by this operation.
/// 
/// The rewriter is located at the beginning of the block on call. All IR
/// mutations must happen through the rewriter.
void mlir::PromotableAllocationOpInterface::handleBlockArgument(const ::mlir::MemorySlot & slot, ::mlir::BlockArgument argument, ::mlir::RewriterBase & rewriter) {
      return getImpl()->handleBlockArgument(getImpl(), getOperation(), slot, argument, rewriter);
  }
/// Hook triggered once the promotion of a slot is complete. This can
/// also clean up the created default value if necessary.
/// This will only be called for slots declared by this operation.
/// 
/// All IR mutations must happen through the rewriter.
void mlir::PromotableAllocationOpInterface::handlePromotionComplete(const ::mlir::MemorySlot & slot, ::mlir::Value defaultValue, ::mlir::RewriterBase & rewriter) {
      return getImpl()->handlePromotionComplete(getImpl(), getOperation(), slot, defaultValue, rewriter);
  }
/// Gets whether this operation loads from the specified slot.
/// 
/// No IR mutation is allowed in this method.
bool mlir::PromotableMemOpInterface::loadsFrom(const ::mlir::MemorySlot & slot) {
      return getImpl()->loadsFrom(getImpl(), getOperation(), slot);
  }
/// Gets the value stored to the provided memory slot, or returns a null
/// value if this operation does not store to this slot. An operation
/// storing a value to a slot must always be able to provide the value it
/// stores. This method is only called on operations that use the slot.
/// 
/// No IR mutation is allowed in this method.
::mlir::Value mlir::PromotableMemOpInterface::getStored(const ::mlir::MemorySlot & slot) {
      return getImpl()->getStored(getImpl(), getOperation(), slot);
  }
/// Checks that this operation can be promoted to no longer use the provided
/// blocking uses, in the context of promoting `slot`.
/// 
/// If the removal procedure of the use will require that other uses get
/// removed, that dependency should be added to the `newBlockingUses`
/// argument. Dependent uses must only be uses of results of this operation.
/// 
/// No IR mutation is allowed in this method.
bool mlir::PromotableMemOpInterface::canUsesBeRemoved(const ::mlir::MemorySlot & slot, const ::llvm::SmallPtrSetImpl<::mlir::OpOperand *> & blockingUses, ::llvm::SmallVectorImpl<::mlir::OpOperand *> & newBlockingUses) {
      return getImpl()->canUsesBeRemoved(getImpl(), getOperation(), slot, blockingUses, newBlockingUses);
  }
/// Transforms IR to ensure that the current operation does not use the
/// provided memory slot anymore. `reachingDefinition` contains the value
/// currently stored in the provided memory slot, immediately before the
/// current operation.
/// 
/// During the transformation, *no operation should be deleted*.
/// The operation can only schedule its own deletion by returning the
/// appropriate `DeletionKind`. The deletion must be legal assuming the
/// blocking uses passed through the `newBlockingUses` list in
/// `canUseBeRemoved` have been removed.
/// 
/// After calling this method, the blocking uses should have disappeared
/// or this operation should have scheduled its own deletion.
/// 
/// This method will only be called after ensuring promotion is allowed via
/// `canUseBeRemoved`. The requested blocking use removal may or may not
/// have been done at the point of calling this method, but it will be done
/// eventually.
/// 
/// The rewriter is located after the promotable operation on call. All IR
/// mutations must happen through the rewriter.
::mlir::DeletionKind mlir::PromotableMemOpInterface::removeBlockingUses(const ::mlir::MemorySlot & slot, const ::llvm::SmallPtrSetImpl<mlir::OpOperand *> & blockingUses, ::mlir::RewriterBase & rewriter, ::mlir::Value reachingDefinition) {
      return getImpl()->removeBlockingUses(getImpl(), getOperation(), slot, blockingUses, rewriter, reachingDefinition);
  }
/// Checks that this operation can be promoted to no longer use the provided
/// blocking uses, in order to allow optimization.
/// 
/// If the removal procedure of the use will require that other uses get
/// removed, that dependency should be added to the `newBlockingUses`
/// argument. Dependent uses must only be uses of results of this operation.
/// 
/// No IR mutation is allowed in this method.
bool mlir::PromotableOpInterface::canUsesBeRemoved(const ::llvm::SmallPtrSetImpl<::mlir::OpOperand *> & blockingUses, ::llvm::SmallVectorImpl<::mlir::OpOperand *> & newBlockingUses) {
      return getImpl()->canUsesBeRemoved(getImpl(), getOperation(), blockingUses, newBlockingUses);
  }
/// Transforms IR to ensure that the current operation does not use the
/// provided blocking uses anymore. In contrast to
/// `PromotableMemOpInterface`, operations implementing this interface
/// must not need access to the reaching definition of the content of the
/// slot.
/// 
/// During the transformation, *no operation should be deleted*.
/// The operation can only schedule its own deletion by returning the
/// appropriate `DeletionKind`. The deletion must be legal assuming the
/// blocking uses passed through the `newBlockingUses` list in
/// `canUseBeRemoved` have been removed.
/// 
/// After calling this method, the blocking uses should have disappeared
/// or this operation should have scheduled its own deletion.
/// 
/// This method will only be called after ensuring promotion is allowed via
/// `canUseBeRemoved`. The requested blocking use removal may or may not
/// have been done at the point of calling this method, but it will be done
/// eventually.
/// 
/// The rewriter is located after the promotable operation on call. All IR
/// mutations must happen through the rewriter.
::mlir::DeletionKind mlir::PromotableOpInterface::removeBlockingUses(const ::llvm::SmallPtrSetImpl<mlir::OpOperand *> & blockingUses, ::mlir::RewriterBase & rewriter) {
      return getImpl()->removeBlockingUses(getImpl(), getOperation(), blockingUses, rewriter);
  }
